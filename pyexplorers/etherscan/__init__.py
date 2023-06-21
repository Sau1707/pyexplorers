from pyexplorers.coin import Coin


class Etherscan(Coin):
    account: None
    contract: None
    transaction: None
    block: None
    logs: None
    proxy: None
    stats: None
    gastracker: None
    
    def __init__(self) -> None:
        super().__init__(
            api="api.etherscan.io/api",
            api_key="542REPGZRRMR8CEP16KD8FM4QUKMGZ78H1"
        )

        # self.stats = Stats(self)