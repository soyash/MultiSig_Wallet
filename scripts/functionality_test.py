from brownie import MultiSigWallet, accounts

def functionality_test():
    msw = MultiSigWallet.deploy({'from':accounts[0]})
    msw.addOwner(accounts[1], {'from':accounts[0]})
    msw.addOwner(accounts[2], {'from':accounts[0]})
    msw.addOwner(accounts[3], {'from':accounts[2]})

    tx1 = msw.submitTransaction(accounts[6], 1, bytes("test_string", 'utf-8'), {'from':accounts[0]})
    print(tx1.events)

    tx2 = msw.approveTransaction(0, {'from':accounts[0]})
    tx3 = msw.approveTransaction(0, {'from':accounts[1]})
    tx4 = msw.approveTransaction(0, {'from':accounts[2]})

    #tx5 = msw.revokeApproval(0, {'from':accounts[2]})

    tx6 = msw.executeTransaction(0, {'from':accounts[0]})


def main():
    functionality_test()