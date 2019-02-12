pragma solidity >=0.4.2 <0.6.0;

contract RockPaperScissors {
    /*  Given a choice (e.g. "rock", "paper" or "scissors")
        and a random/blinding string, returns a commitment
        of the pair. Note calls to this function occur offline
        (i.e. do not appear on the blockchain).
        If you leave the 'pure'keyword in the function signature,
        function calls to this won't publish to the blockchain.
    */ 
    function encode_commitment(string memory choice, string memory rand)
    public pure returns (bytes32) {

    }

    /*  Accepts a commitment (generated via encode_commitment)
        and a wage of ethereum
    */
    function play(bytes32 commitment) public payable {

    }

    /*  Once both players have commited (called play()),
        they reveal their choice and blinding string.
        This function verifies the commitment is correct
        and after both players submit, determines the winner.
    */
    function reveal(string memory choice, string memory rand) public {

    }

    /*  After both players reveal, this allows the winner
        to claim their reward (both wagers).
        In the event of a tie, this function should let
        each player withdraw their initial wager
    */
    function withdraw() public {
        
    }
}