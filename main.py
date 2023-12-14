from blockchain import Blockchain
from wallet import Wallet

def main():
    # Initialize blockchain
    my_blockchain = Blockchain()

    # Create two wallets
    wallet1 = Wallet()
    wallet2 = Wallet()

    # Check if addresses are different
    if wallet1.address == wallet2.address:
        print("Error: Duplicate addresses generated.")
        return
    else:
        print("Unique addresses confirmed.")

    # Display wallet addresses
    print(f"Wallet 1 Address: {wallet1.address}")
    print(f"Wallet 2 Address: {wallet2.address}")

    # Wallet 1 sends money to Wallet 2
    wallet1.send_money(wallet2.address, 50, my_blockchain)

    # Mine pending transactions
    my_blockchain.mine_unconfirmed_transactions()

    # Check if the blockchain is valid
    print(f"Is Blockchain valid? {my_blockchain.is_chain_valid()}")

    # Display the blockchain
    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        for transaction in block.transactions:
            print(f"    Sender: {transaction.sender}")
            print(f"    Receiver: {transaction.receiver}")
            print(f"    Amount: {transaction.amount}")
        print(f"    Hash: {block.hash}")

if __name__ == "__main__":
    main()
