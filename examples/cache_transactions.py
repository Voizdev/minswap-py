"""Build a transaction cache.

The goal of this script is to build a transaction cache. Use this with caution.
Blockfrost will ban an account that tries to maliciously overuse their API based on the
limits permitted for the account.

Built into the caching functions are two levels of rate limiters designed to prevent
Blockfrost issues.

The first is a `max_calls` input, which limits the maximum number of calls that will be
made. For a free account on Blockfrost, 50,000 requests/day are permitted. This is not
an intelligent system. The function will stop when Blockfrost returns an error code or
when all available transactions have been acquired. It is up to the user to not
repeatedly call the caching functions if an error code is returned from Blockfrost.

The second is a rate limiting step, that pauses requests when they are being made too
quickly. Blockfrost allows 10 calls/second, with 500 request bursts and a 10 call/second
regeneration. This means that 500 requests can be sent at once, but then there is a 50
second cooloff period before additional requests can be made. The caching code tries to
account for this and will pause requests when getting near this limit. A warning is
shown to indicate to the user that the code is waiting to cooloff, and this is expected
behavior that can be ignored in most cases.
"""
import logging
import time

from minswap.assets import asset_ticker
from minswap.pools import get_pools
from minswap.transactions import cache_transactions

# Just to see what minswap-py is doing under the hood...
logging.getLogger("minswap").setLevel(logging.DEBUG)

# Maximum number of API calls allowed for this script to run
# If only using this to update transactions once per day, and it's the only code using
# Blockfrost, this can be set to 50,000 for a free account.
max_calls = 20000
total_calls = 0

# Get a list of pools
pools = get_pools()
assert isinstance(pools, list)

# Iterate over the pools and cache transations
for pool in pools:
    if total_calls >= max_calls:
        print("Reached maximum requests. Exiting script.")
        break

    print(
        "Getting transaction for pool: "
        + f"{asset_ticker(pool.unit_a)}-{asset_ticker(pool.unit_b)}"
    )
    calls = cache_transactions(pool.id, max_calls - total_calls, True)

    cooloff = min(50, calls / 10)
    print(f"Made {calls} calls. Cooling off {cooloff:0.2f}s before starting next pool")
    time.sleep(cooloff)

    total_calls += calls