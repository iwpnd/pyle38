# Changelog

<!--next-version-placeholder-->

## v0.8.1 (2023-01-25)
### Fix
* 🐛 fset when field value is object ([`c16f487`](https://github.com/iwpnd/pyle38/commit/c16f4873948d2f1f4fc8be314ff268a6479b5b3b))

## v0.8.0 (2022-12-22)
### Feature
* ✨ allow field Any field value ([`ddc3f4a`](https://github.com/iwpnd/pyle38/commit/ddc3f4a34807d801a3c98ed452e0bd355b641caf))
* ✨ add test helpers ([`277679b`](https://github.com/iwpnd/pyle38/commit/277679b65de53711fc4ee711ff4477562f23bd84))
* ✨ implement whereable ([`65fa065`](https://github.com/iwpnd/pyle38/commit/65fa0652d24c77dd02eeb9f1c1057a236d305fa2))

### Fix
* 🐛 rename to where_expr ([`8002e6a`](https://github.com/iwpnd/pyle38/commit/8002e6a627a95b1e7ddada7ca422bff7818d5484))
* 🐛 add whereable ([`1194a70`](https://github.com/iwpnd/pyle38/commit/1194a70ab21a82ac870a369abf22869822832312))

### Documentation
* Fix ([`d792507`](https://github.com/iwpnd/pyle38/commit/d792507be425151d9a63ef49af356143f499d519))
* 📚️ update readme ([`001f719`](https://github.com/iwpnd/pyle38/commit/001f719c7ab7c1240ec9a18a0afef1f956e2a22d))

## v0.7.0 (2022-09-06)
### Feature
* ✨ upgrade to redis-py, use single connection instead of pool ([`b31136d`](https://github.com/iwpnd/pyle38/commit/b31136d0d18b9d78d6a286abaab0e2ba3b33f6c0))

## v0.6.1 (2022-01-24)
### Fix
* 🐛 generic types and defaults ([`45fcd5d`](https://github.com/iwpnd/pyle38/commit/45fcd5d6574242943d35ad5712403bbe1e70c81c))

### Documentation
* 📚️ new logo ([`d0c95d3`](https://github.com/iwpnd/pyle38/commit/d0c95d394dc584f2625e4c2c7206cd509ae3498f))

## v0.6.0 (2022-01-04)
### Feature
* ✨ add buffer search option to within search ([`1ad3655`](https://github.com/iwpnd/pyle38/commit/1ad3655c022b67f6b1a33928219641818974e152))
* ✨ add buffer search option to intersects search ([`f23d800`](https://github.com/iwpnd/pyle38/commit/f23d8002b3fcefef242d0cd1ec8bbaec656fef15))

### Documentation
* 📚️ update readme ([`4b57fbf`](https://github.com/iwpnd/pyle38/commit/4b57fbfadd5e7bb89797801f8e516f317effaa19))

## v0.5.1 (2021-11-21)
### Fix
* 🐛 remove stringobject class in favour of generics ([`8317d40`](https://github.com/iwpnd/pyle38/commit/8317d40420b4625ea2b95b392da49177e817a1ef))
* 🐛 utilize generic model object ([`1f95d2c`](https://github.com/iwpnd/pyle38/commit/1f95d2c6d9adb06871749468991c9f38c5d5d6eb))
* 🐛 get as string object ([`9f1a3a3`](https://github.com/iwpnd/pyle38/commit/9f1a3a3eb17a196538938d9c6cb27a19b3fe18eb))

### Documentation
* 📚️ update docs ([`04cad31`](https://github.com/iwpnd/pyle38/commit/04cad3155a9b103eef8f121f6d10a1910d796260))

## v0.5.0 (2021-10-04)
### Feature
* ✨ add sector search to within and intersects ([`4b6931b`](https://github.com/iwpnd/pyle38/commit/4b6931ba59d9c4a573a7e54452b74bc640cac0e1))

## v0.4.0 (2021-09-10)
### Feature
* ✨ add where filter to scan command ([`8c78d8b`](https://github.com/iwpnd/pyle38/commit/8c78d8b54ba4554b433334f98eaaf00110fe3b99))
* ✨ add where filter to search command ([`5e02bd4`](https://github.com/iwpnd/pyle38/commit/5e02bd40711021a09bb1db6c6ece561af707ecd8))
* ✨ add where filter to nearby command ([`0f795c8`](https://github.com/iwpnd/pyle38/commit/0f795c878ff8c84d41a712643ae773aba25b7b04))
* ✨ add where filter to intersects command ([`dbf8be1`](https://github.com/iwpnd/pyle38/commit/dbf8be14697f2f422e462e90140b66ce17a5a7c3))
* ✨ add where filter to within command ([`ceb5a29`](https://github.com/iwpnd/pyle38/commit/ceb5a29aad148c96729da8b2879fbec6a5d30605))

### Fix
* 🐛 update server extended response ([`62628fb`](https://github.com/iwpnd/pyle38/commit/62628fb14b0444a381fe2da3b59e384ad39460de))

### Documentation
* 📚️ update docs ([`8a7cec2`](https://github.com/iwpnd/pyle38/commit/8a7cec286ee472361a7c2e1c7ec8c974f4a8ae71))
* 📚️ update docs ([`4fcc6e6`](https://github.com/iwpnd/pyle38/commit/4fcc6e664fc229d68465a0cca34e9ae4c48ddd62))
* Update readme, fix typo ([`e4a02f2`](https://github.com/iwpnd/pyle38/commit/e4a02f2c21d651d8b7bc4aa19cfaeef1ead87898))
* 📚️ update readme ([`d318051`](https://github.com/iwpnd/pyle38/commit/d3180518c799897c8c0f65af80c669bc04c89f90))
* 📚️ update docs, add logo ([`09b44e2`](https://github.com/iwpnd/pyle38/commit/09b44e2071d79d26ed04faa1b26d53625ea15f82))

## v0.3.2 (2021-07-31)

-   🔧 update aioredis to v2.0.0
-   🔧 update tile38 to v1.25.1

## v0.3.1 (2021-07-25)

### Fix

-   🐛 redis from url is sync ([`7842e76`](https://github.com/iwpnd/pyle38/commit/7842e76a9bd870709030a4d5779d22d4faa18f0d))

### Documentation

-   📚️ remove duplicated changelog entries [skip ci] ([`9743221`](https://github.com/iwpnd/pyle38/commit/9743221c33282b9fc8206275f6cc3a6922efa886))

## v0.3.0 (2021-06-27)

### Feature

-   ✨ add INFO command ([`3e3d916`](https://github.com/iwpnd/pyle38/commit/3e3d9160d0f8dbc6409beab373234f0e6009683a))

### Fix

-   🐛 incompatible return types on subclass follower ([`600e59f`](https://github.com/iwpnd/pyle38/commit/600e59f915c39d59a57c5d17570e29a5c24d7807))
