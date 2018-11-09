"""Pull data from geth and parse it into mongo."""

import subprocess
import sys
sys.path.append("./../analysis")
sys.path.append("./../preprocessing/Crawler")
import os
os.environ['ETH_BLOCKCHAIN_ANALYSIS_DIR'] = './../preprocessing'
from Crawler import Crawler
sys.path.append("./../preprocessing")  # has to go after Crawler import
from ContractMap import ContractMap
import subprocess
import time
LOGDIR = "./../preprocessing/logs"

subprocess.call([
    # "(geth --rpc --rpcport 8545 > {}/geth.log 2>&1) &".format(LOGDIR),  # original
    "(geth --testnet --rpc --syncmode fast --cache=2048 > {}/geth.log 2>&1) &".format(LOGDIR),  # new
    # "(mongod --dbpath mongo/data --port 27017 > {}/mongo.log 2>&1) &".format(LOGDIR)  # old
    "(mongod --dbpath " + os.environ['BLOCKCHAIN_MONGO_DATA_DIR'] + " --port 27017 > {}/mongo.log 2>&1) &".format(LOGDIR)
], shell=True)

print("Booting processes.")
# Catch up with the crawler
c = Crawler()

print("Updating contract hash map.")
# Update the contract addresses that have been interacted with
ContractMap(c.mongo_client, last_block=c.max_block_mongo)

print("Update complete.")
subprocess.call([
    # "(geth --rpc --rpcport 8545 > {}/geth.log 2>&1) &".format(LOGDIR),  # old
    "(geth --testnet --rpc --syncmode fast --cache=2048 > {}/geth.log 2>&1) &".format(LOGDIR),  # new
    # "(mongod --dbpath mongo/data --port 27017 > {}/mongo.log 2>&1) &".format(LOGDIR)  # old
    "(mongod --dbpath " + os.environ['BLOCKCHAIN_MONGO_DATA_DIR'] + " --port 27017 > {}/mongo.log 2>&1) &".format(LOGDIR)  # new
], shell=True)
