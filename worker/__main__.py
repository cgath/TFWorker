import os, sys
from azure.storage.blob import BlockBlobService

def main(args=None):
    """The main routine."""
    
    if args is None:
        args = sys.argv[1:]
    
    # Get connection string from env var
    account_name = os.environ['AZURE_ACC_NAME']
    account_key = os.environ['AZURE_ACC_KEY']

    # TODO: Parse args:

        # get container name ...
        # get blob name ...

        # get first sample index ...
        # get number of samples to read ...
        
        # get number of wavelengths ...
        # get number of refs/sample ...

    print('account_name: {}'.format(account_name))
    print('account_key: {}'.format(account_key))

if __name__ == "__main__":
    main()
