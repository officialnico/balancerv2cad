## Setup:

go into the root of the dir after cloning

```
git clone https://github.com/balancer-labs/balancer-core-v2.git
mv package.json balancer-core-v2
cd balancer-core-v2
yarn
yarn test
```

to run tests:
from the balancerV2_Model/balancer-core-v2 directory

`yarn test`

to debug the results go to the contracts and find the contract you are looking for and put this after all the imports

`import "hardhat/console.sol";`

to print the value of a variable you can use `console.log(...);` under it. you may have to change the 'pure' after the functions parameters to a 'view', you will also have to do it for the Mock contract, and you might even have to for any functions called in the way.
