[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)


## Setup:


go into the root of the dir after cloning

- have node installed (check with `npm -v`)
-  have yarn installed (`npm install -g yarn`)

```
git clone https://github.com/balancer-labs/balancer-core-v2.git
cp package.json balancer-core-v2
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

if you feel lost run `yarn test` and go to the error where 'pure' is showing up (if this is the error), and change it to a view
