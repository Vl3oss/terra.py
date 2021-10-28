from terra_sdk.client.lcd import LCDClient, PaginationOptions

def main():
    terra = LCDClient(
        url="https://bombay-lcd.terra.dev/",
        chain_id="bombay-12",
    )

    pagOpt = PaginationOptions(limit=2)

    result = terra.gov.proposals()
    print("whole proposals", result)
    result = terra.gov.proposals(PaginationOptions(limit=2))
    print("first 2 params", result)
    #result = terra.gov.proposal(1)      # FIXME: not working.. tx.height
    print(result)
    #result = terra.gov.deposits(1)       # FIXME: tx.height problem
    print(result)
    result = terra.gov.votes(5333, pagOpt)
    print(result)
    result = terra.gov.tally(5333)
    print(result)
    result = terra.gov.deposit_parameters()
    print(result)
    result = terra.gov.voting_parameters()
    print(result)
    result = terra.gov.tally_parameters()
    print(result)
    result = terra.gov.parameters()
    print(result)

main()