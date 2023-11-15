decision_tree = {
    "choice": "blockchain",
    "starting_point": "blockchain_type",
    "blockchain_type": {
        "question": "What's your blockchain type?",
        "answers": ["public", "private"],
        "next_question": {
            "public": "decentralization_level",
            "private": "main_priority"
        }
    },

    "main_priority": {
        "question": "Is safety you main priority?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "price",
            "no": "ANSWER Hyperledger"
        }
    },

    "price": {
        "question": "Is price essential to you?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "ANSWER R3 Corda",
            "no": "ANSWER Hyperledger"
        }
    },

    "decentralization_level": {
        "question": "Is high decentralization level critical to you?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "attacks",
            "no": "ANSWER Tron"
        }
    },

    "attacks": {
        "question": "Is it unacceptable for you if there were any successful attacks on the blockchain?",
        "answers": ["unacceptable", "acceptable"],
        "next_question": {
            "unacceptable": "energy_use",
            "acceptable": "ANSWER Tron"
        }
    },

    "code": {
        "question": "Do you plan to write dApps based on the blockchain a lot?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "trans_amount",
            "no": "ANSWER Bitcoin"
        }
    },

    "energy_use": {
        "question": "Is minimizing energy use important to you?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "code",
            "no": "ANSWER Bitcoin"
        }
    },

    "trans_amount": {
        "question": "Do you plan to send a considerably high amount of transactions per a small period of time?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "users_amount",
            "no": "trans_price"
        }
    },

    "trans_price": {
        "question": "Is transaction price essential to you?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "capacity",
            "no": "ANSWER Ethereum"
        }
    },

    "capacity": {
        "question": "Do you focus on a great capacity for your network?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "ANSWER Optimism",
            "no": "ANSWER Ethereum"
        }
    },

    "users_amount": {
        "question": "Are you planning to interact with a huge amount of users?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "nft",
            "no": "trans_price"
        }
    },

    "nft": {
        "question": "Are you going to use many NFTs?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "ANSWER Polygon",
            "no": "evm"
        }
    },

    "evm": {
        "question": "Does the network have to be EVM-compatible?",
        "answers": ["yes", "no"],
        "next_question": {
            "yes": "ANSWER Avalanche",
            "no": "ANSWER Solana"
        }
    },
}
