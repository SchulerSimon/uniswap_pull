from web3 import Web3

"""
template = {
    "template": {
        "token_contract": Web3.toChecksumAddress("template"),
        "exchange_contract": Web3.toChecksumAddress("template")
    },
}
"""

mappings = {
    "sETH": {
        "token_contract": Web3.toChecksumAddress(
            "0x5e74c9036fb86bd7ecdcb084a0673efc32ea31cb"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0xe9cf7887b93150d4f2da7dfc6d502b216438f244"
        ),
    },
    "MKR": {
        "token_contract": Web3.toChecksumAddress(
            "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x2c4bd064b998838076fa341a83d007fc2fa50957"
        ),
    },
    "SAI": {
        "token_contract": Web3.toChecksumAddress(
            "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x09cabec1ead1c0ba254b09efb3ee13841712be14"
        ),
    },
    "WETH": {
        "token_contract": Web3.toChecksumAddress(
            "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0xa2881a90bf33f03e7a3f803765cd2ed5c8928dfb"
        ),
    },
    "SNX": {
        "token_contract": Web3.toChecksumAddress(
            "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x3958b4ec427f8fa24eb60f42821760e88d485f7f"
        ),
    },
    "DAI": {
        "token_contract": Web3.toChecksumAddress(
            "0x6b175474e89094c44da98b954eedeac495271d0f"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x2a1530c4c41db0b0b2bb646cb5eb1a67b7158667"
        ),
    },
    "USDC": {
        "token_contract": Web3.toChecksumAddress(
            "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x97dec872013f6b5fb443861090ad931542878126"
        ),
    },
    "WBTC": {
        "token_contract": Web3.toChecksumAddress(
            "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x4d2f5cfba55ae412221182d8475bc85799a5644b"
        ),
    },
    "BAT": {
        "token_contract": Web3.toChecksumAddress(
            "0x0d8775f648430679a709e98d2b0cb6250d2887ef"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0x2e642b8d59b45a1d8c5aef716a84ff44ea665914"
        ),
    },
    "sUSD": {
        "token_contract": Web3.toChecksumAddress(
            "0x57ab1ec28d129707052df4df418d58a2d46d5f51"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0xb944d13b2f4047fc7bd3f7013bcf01b115fb260d"
        ),
    },
    "TKN": {
        "token_contract": Web3.toChecksumAddress(
            "0xaaaf91d9b90df800df4f55c205fd6989c977e73a"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0xb6cfbf322db47d39331e306005dc7e5e6549942b"
        ),
    },
    "LRC": {
        "token_contract": Web3.toChecksumAddress(
            "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd"
        ),
        "exchange_contract": Web3.toChecksumAddress(
            "0xa539baaa3aca455c986bb1e25301cef936ce1b65"
        ),
    },
}
