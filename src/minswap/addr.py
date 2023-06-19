"""Important Cardano addresses for Minswap.

These are addresses for pools and smart contracts associated with Minswap.

Attributes:
    POOL: Mainnet pool address.
    POOL_TEST: Testnet pool address.
    ORDER: Mainnet pool address.
    ORDER_TEST: Testnet pool address.
"""

from minswap.models import Address

POOL = Address(
    bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha"  # noqa
)

#Added a new POOLS list to reference instead of the single POOL constant
POOLS = [
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha"),
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxzfgf0jgfz5xdvg2pges20usxhw8zwnkggheqrxwmxd6huuqss46eh"), #AGIX
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxzwccf8ywaly0m99ngq68lus48lmafut7ku9geawu8u6k49suv42qq"), #WMT
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz02znpd777wgl9wwpk0dvdzuxn93mqh82q7vv6s9jn25rws52z94g"), #iUSD
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2jyskd3y6etkv8ye450545xu6q4jfq5hv4e0uxwkpf8lsq048y90"), #AADA
    Address(bech32="addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxztnqm37tpj0q63s0qns5wfe4flqzqqg55760472n7yt4v8skpaj3k") #SNEK
]

ORDER = Address(bech32="addr1wxn9efv2f6w82hagxqtn62ju4m293tqvw0uhmdl64ch8uwc0h43gt")

POOL_TEST = Address(
    bech32="addr_test1zrsnz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxzvrajt8r8wqtygrfduwgukk73m5gcnplmztc5tl5ngy0upqs8q93k"  # noqa
)
ORDER_TEST = Address(
    bech32="addr_test1wzn9efv2f6w82hagxqtn62ju4m293tqvw0uhmdl64ch8uwc5lpd8w"
)

# Policies
FACTORY_POLICY_ID = "13aa2accf2e1561723aa26871e071fdf32c867cff7e7d50ad470d62f"
FACTORY_ASSET_NAME = "4d494e53574150"
LP_POLICY_ID = "e4214b7cce62ac6fbba385d164df48e157eae5863521b4b67ca71d86"
POOL_NFT_POLICY_ID = "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1"
