"""Util functions for Analysis process."""
import os


def set_env():
    """Set the analysis environment directory."""
    env = {
            "mongo": ".",      # Where the mongo data is stored
            "txn_data": "/home/justin/data"    # Where the TxnGraphs are stored
        }
    if 'BLOCKCHAIN_MONGO_DATA_DIR' in os.environ:
        env["mongo"] = os.environ['BLOCKCHAIN_MONGO_DATA_DIR']
    else:
        os.environ['BLOCKCHAIN_MONGO_DATA_DIR'] = '/var/lib/mongodb/'  # new

    if 'BLOCKCHAIN_DATA_DIR' in os.environ:
        env["tnx_data"] = os.environ['BLOCKCHAIN_DATA_DIR']

    if 'BLOCKCHAIN_ANALYSIS_LOGS' not in os.environ:
        os.environ['BLOCKCHAIN_ANALYSIS_LOGS'] = '/home/justin/Dropbox/projects/python/crypto_arb/code/ethereum_chain_parser/preprocessing/logs'

    return env
