# CHANGELOG


## v0.14.0 (2024-11-14)

### Build System

- 📦️ update
  ([`5af6900`](https://github.com/iwpnd/pyle38/commit/5af69008390fcfb3740b01285020a3e8e8e3c598))

### Chores

- **deps**: 🔗 update redis
  ([`6b3ebbd`](https://github.com/iwpnd/pyle38/commit/6b3ebbde0a2b8556fbf78619fd4a99064dc22ac1))

### Documentation

- 📚️ update readme
  ([`2989d82`](https://github.com/iwpnd/pyle38/commit/2989d82ffcec92ddd9f20109789908e63dc3afbb))

- 📚️ moar docstrings
  ([`a9b2277`](https://github.com/iwpnd/pyle38/commit/a9b2277a8a874f01d5cc394d3c52e7eadfddecdd))

### Features

- ✨ client connection options
  ([`a4b0011`](https://github.com/iwpnd/pyle38/commit/a4b0011fa70c58960310f8fa294ab70d10a256b5))

using options pattern redis client connection options

closes #529

### Refactoring

- ♻️ make client url private, but backward compatible
  ([`651f7b3`](https://github.com/iwpnd/pyle38/commit/651f7b3ec6fee448be8534c6f7a28582c4fada19))

- ♻️ make client url private
  ([`e72b441`](https://github.com/iwpnd/pyle38/commit/e72b4413f058cc83d898569862d3ac336e15e854))

- ♻️ drop variable position arguments, add missing docstrings
  ([`d4c0294`](https://github.com/iwpnd/pyle38/commit/d4c0294a0a49d93b53f1ab7daf5b7cdc9ad31081))


## v0.13.3 (2024-11-01)

### Refactoring

- ♻️ set Tile38 output to JSON on_connect
  ([`5491580`](https://github.com/iwpnd/pyle38/commit/5491580d7ea134f75f0ec851ca76ccc8d1e4337b))

instead of maintaining a `__format` state that needs to be validated and updated on every state of
  the connection.

Co-authored-by: Alex Ward <alxwrd@googlemail.com>


## v0.13.2 (2024-11-01)

### Bug Fixes

- 🐛 reset format on .quit() to allow re-connect on same instance
  ([`fe5986b`](https://github.com/iwpnd/pyle38/commit/fe5986b8ff8894e3bb4d5509fb38b6b014370ce2))

Co-authored-by: Alex Ward <alxwrd@googlemail.com>


## v0.13.1 (2024-11-01)

### Bug Fixes

- Tile38 format not resetting on reconnect
  ([`8a16d4a`](https://github.com/iwpnd/pyle38/commit/8a16d4a8f73accd05233abd0b9b4c5ad200a7dd0))

Co-authored-by: Alex Ward <alxwrd@googlemail.com>

### Chores

- **deps**: Bump python-semantic-release/python-semantic-release
  ([`f39be83`](https://github.com/iwpnd/pyle38/commit/f39be832a723fdb534a07a123028631479c24f07))

Bumps
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.9.0 to 9.12.0. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.9.0...v9.12.0)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis
  ([`a9e944a`](https://github.com/iwpnd/pyle38/commit/a9e944aff1e3a542b036ede287b804357b3d640b))

- **deps**: Bump pydantic
  ([`7e14731`](https://github.com/iwpnd/pyle38/commit/7e147317cb943fe0ba2ff42dc20d2b33f53d1644))

- **deps**: Bump python-semantic-release/python-semantic-release
  ([`7e8c3fb`](https://github.com/iwpnd/pyle38/commit/7e8c3fbb386f2112d299d7bb5eedc7e05d3b69b4))

Bumps
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.8.6 to 9.8.7. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.6...v9.8.7)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: 🔗 update redis to 5.0.8
  ([`819fca0`](https://github.com/iwpnd/pyle38/commit/819fca0a3eca1834ee1c381b78d787ed09a5422c))

- **deps**: Bump snok/install-poetry from 1.3 to 1.4
  ([`5132b28`](https://github.com/iwpnd/pyle38/commit/5132b28b62d29d2391e90b64123639e83a516591))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.3 to 1.4. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.3...v1.4)

--- updated-dependencies: - dependency-name: snok/install-poetry dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: 🔗 bump pydantic
  ([`403229b`](https://github.com/iwpnd/pyle38/commit/403229b6d315002f8c169051dd6bfc3c63191cd1))

- **deps**: Bump python-semantic-release/python-semantic-release
  ([`c76e12e`](https://github.com/iwpnd/pyle38/commit/c76e12ec66cf7ab4d5c5af470782bc4b493bfd20))

Bumps
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.8.0 to 9.8.3. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.0...v9.8.3)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: 🔗 bump redis and pydantic
  ([`8c15fb9`](https://github.com/iwpnd/pyle38/commit/8c15fb9a29c95b4a98b2c49f0567afe7ddca1774))


## v0.13.0 (2024-06-22)

### Chores

- **deps**: Update
  ([`af90370`](https://github.com/iwpnd/pyle38/commit/af90370c8d76415db7af2c16b48b7ca8dac87fa8))

- **deps**: Update
  ([`3d9f7c4`](https://github.com/iwpnd/pyle38/commit/3d9f7c4e535ad4412679b358d2279c4a0409f937))

### Documentation

- Update with WHEREIN
  ([`03c0599`](https://github.com/iwpnd/pyle38/commit/03c059931aa6c2d5ebedde630c50c29014baa25b))

### Features

- Add WHEREIN to SEARCH
  ([`e7b5c29`](https://github.com/iwpnd/pyle38/commit/e7b5c297d4f40213cdc2d1131a1416ee4644bfeb))

- Add WHEREIN to NEARBY
  ([`587c629`](https://github.com/iwpnd/pyle38/commit/587c6292180a66e709983e38ccfa56fa00318b77))

- Add WHEREIN to INTERSECTS
  ([`41e81dd`](https://github.com/iwpnd/pyle38/commit/41e81dd356816dc4f5f069315e756e11767aec3e))

- Add WHEREIN to WITHIN
  ([`f706b80`](https://github.com/iwpnd/pyle38/commit/f706b809046f8db41bbfc35482a860945d71b065))

- Add WHEREIN to SCAN
  ([`afa301e`](https://github.com/iwpnd/pyle38/commit/afa301e6cfd8fef9db04275bf1ebf4d4b6ede999))

- Add wherein to Whereable class
  ([`c3ad4df`](https://github.com/iwpnd/pyle38/commit/c3ad4df2ddaa74663b0f65e0a0d57812dff83f7a))

### Refactoring

- Simplify WHEREIN command, resolve mypy issues on object searches
  ([`33b23e8`](https://github.com/iwpnd/pyle38/commit/33b23e8432da2a55bbde3045f12e5dd7265a6c7b))


## v0.12.0 (2024-06-07)

### Documentation

- Update docs for EXISTS and FEXISTS
  ([`f9bca32`](https://github.com/iwpnd/pyle38/commit/f9bca32f1a6806eb4a7e996235b252ba11ef5aff))

### Features

- Support FEXISTS command as of tile38 v1.33.0
  ([`12f900d`](https://github.com/iwpnd/pyle38/commit/12f900dab4f39c49d19e87c4fd64f8a9ee887676))

- Support EXISTS command as of tile38 v1.33.0
  ([`39e0593`](https://github.com/iwpnd/pyle38/commit/39e0593fa3cddfceff30a39998146114d6e1cc4f))


## v0.11.4 (2024-06-07)

### Bug Fixes

- Objectresponse with fields not compatible with Tile38 v1.30.0
  ([`6272e70`](https://github.com/iwpnd/pyle38/commit/6272e70f5bb22833aa3363073d2bfb121aee1cf2))

### Chores

- **deps**: Bump python-semantic-release/python-semantic-release
  ([`3578319`](https://github.com/iwpnd/pyle38/commit/357831983e50c0824fdad31ffab7807e49952551))

Bumps
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.6.0 to 9.8.0. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.6.0...v9.8.0)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: 🔗 update redis
  ([`7f52479`](https://github.com/iwpnd/pyle38/commit/7f524794a963b29f715fede2688db3befdbb1611))


## v0.11.3 (2024-05-05)

### Bug Fixes

- Bump pydantic to v2.7.0
  ([`f71b6c6`](https://github.com/iwpnd/pyle38/commit/f71b6c6d836f1a9debe136472eae20039acba1fa))

### Chores

- **deps**: Update redis
  ([`c7e2b1e`](https://github.com/iwpnd/pyle38/commit/c7e2b1ec1d7de8e5b2456754e2c70e94bb4126b9))

- **deps**: Bump actions/cache from 4.0.0 to 4.0.1
  ([`ff3161e`](https://github.com/iwpnd/pyle38/commit/ff3161e74c3344dd92d49e94f2e42acf589d457f))

Bumps [actions/cache](https://github.com/actions/cache) from 4.0.0 to 4.0.1. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v4.0.0...v4.0.1)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump python-semantic-release/python-semantic-release
  ([`b772a6b`](https://github.com/iwpnd/pyle38/commit/b772a6b460cdd26614d49a4ad0db8f77819e660c))

Bumps
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.1.0 to 9.1.1. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.1.0...v9.1.1)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Update pydantic
  ([`bffbe1c`](https://github.com/iwpnd/pyle38/commit/bffbe1c7c649014861013a3d0226e921d22ff9a9))

- **deps**: Update pydantic
  ([`2eb7986`](https://github.com/iwpnd/pyle38/commit/2eb7986315297c2b45295b6bdc144ab338725a1c))

- **deps**: 🔗 remove black, update pydantic
  ([`0b59dd7`](https://github.com/iwpnd/pyle38/commit/0b59dd7bd7188ecb44de11b15084cbfc55f43066))

- **deps**: Update
  ([`0ce11c4`](https://github.com/iwpnd/pyle38/commit/0ce11c43486676504eda57422e3cd4dadafe84c3))


## v0.11.2 (2024-01-09)

### Bug Fixes

- Use aclose to close connection instead of deprecated close()
  ([`2df87b5`](https://github.com/iwpnd/pyle38/commit/2df87b52c4d8d32d6101a522cff374959f59789e))

### Chores

- **deps**: Bump pydantic from 2.5.1 to 2.5.2
  ([`9d26cc8`](https://github.com/iwpnd/pyle38/commit/9d26cc8b8eafb2dbb018c48b245fb4b2bb078611))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.5.1 to 2.5.2. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v2.5.2/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.5.1...v2.5.2)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.5.0 to 2.5.1
  ([`5cb4d03`](https://github.com/iwpnd/pyle38/commit/5cb4d03fc87c9bc9901700c9846ef5533d974470))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.5.0 to 2.5.1. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.5.0...v2.5.1)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.4.2 to 2.5.0
  ([`7b4456c`](https://github.com/iwpnd/pyle38/commit/7b4456ca1f727003a33cc1a7d6063fae1d3bfffe))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.4.2 to 2.5.0. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.4.2...v2.5.0)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.4.1 to 2.4.2
  ([`e4c1ef4`](https://github.com/iwpnd/pyle38/commit/e4c1ef42c1f472fdae9fd581a5629116c49871f5))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.4.1 to 2.4.2. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.4.1...v2.4.2)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.3.1 to 3.3.2
  ([`d9a2ad5`](https://github.com/iwpnd/pyle38/commit/d9a2ad5eef781b09c9a6ae7cbdb9b9a835c5f811))

Bumps [actions/cache](https://github.com/actions/cache) from 3.3.1 to 3.3.2. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.3.1...v3.3.2)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/checkout from 3 to 4
  ([`e991811`](https://github.com/iwpnd/pyle38/commit/e991811e10af9d943f85872b97f2eb224b00bdb6))

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4. - [Release
  notes](https://github.com/actions/checkout/releases) -
  [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/actions/checkout/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/checkout dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 5.0.0 to 5.0.1
  ([`0639456`](https://github.com/iwpnd/pyle38/commit/0639456d6ab9ccb56fd3ce8091e1ecce0bb4f7cf))

Bumps [redis](https://github.com/redis/redis-py) from 5.0.0 to 5.0.1. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v5.0.0...v5.0.1)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.4.0 to 2.4.1
  ([`41153a8`](https://github.com/iwpnd/pyle38/commit/41153a86b10803427a2ccddb07b390fd2e880ae0))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.4.0 to 2.4.1. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.4.0...v2.4.1)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.3.0 to 2.4.0
  ([`7701b1f`](https://github.com/iwpnd/pyle38/commit/7701b1f64c03df96c7388ae4caa35e5b010ed564))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.3.0 to 2.4.0. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.3.0...v2.4.0)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.11.1 (2023-09-05)

### Bug Fixes

- 🐛 update redis to v5
  ([`a5290ae`](https://github.com/iwpnd/pyle38/commit/a5290aec652cf697d23cf007cb054ea9be8c31ee))

### Chores

- **deps**: Bump pydantic from 2.2.0 to 2.3.0
  ([`3ac4690`](https://github.com/iwpnd/pyle38/commit/3ac4690c7ec1b0dd3ee4714ed1a17d91f6abc32f))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.2.0 to 2.3.0. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.2.0...v2.3.0)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 2.1.1 to 2.2.0
  ([`6a710fe`](https://github.com/iwpnd/pyle38/commit/6a710fe54e8d800c2e70383d4490ffa0e5a3d9d2))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.1.1 to 2.2.0. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.1.1...v2.2.0)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.11.0 (2023-08-08)

### Chores

- **deps**: Bump pydantic from 2.0.3 to 2.1.1
  ([`886e91a`](https://github.com/iwpnd/pyle38/commit/886e91aa04e461e3b6c447a0bee985ca518e8876))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 2.0.3 to 2.1.1. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v2.0.3...v2.1.1)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- 📚️ docstring
  ([`c295aee`](https://github.com/iwpnd/pyle38/commit/c295aee085243205860e4619127ed659275b5ed1))

start adding some docstrings closes #310

- 📚️ update
  ([`45473e3`](https://github.com/iwpnd/pyle38/commit/45473e3b9f0144c1bbd67f02436b031edb235c4a))

### Features

- ✨ add z coordinate to set and get point
  ([`3b4bd85`](https://github.com/iwpnd/pyle38/commit/3b4bd85bc6e2acba331bdf9806cb3f3f939a2e5d))

- ✨ release v0.10.0
  ([`ace3647`](https://github.com/iwpnd/pyle38/commit/ace36479e0d02ab5d8e534736a514f7bfd73b403))


## v0.10.0 (2023-07-16)

### Bug Fixes

- 🐛 model_config
  ([`d8e7d59`](https://github.com/iwpnd/pyle38/commit/d8e7d594a16a2006181bee75a8011e3a02a43cc3))

- 🐛 incompatible types in assignment
  ([`8a70323`](https://github.com/iwpnd/pyle38/commit/8a70323b89d8b3c2703645a4e2fbc06c292b9b3a))

### Chores

- **deps**: Bump pydantic from 1.10.8 to 1.10.9
  ([`fa1116b`](https://github.com/iwpnd/pyle38/commit/fa1116bfd02fad02bcd2058fc06230a197e7c97b))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.8 to 1.10.9. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.8...v1.10.9)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 3.1.3 to 3.1.4
  ([`5abc552`](https://github.com/iwpnd/pyle38/commit/5abc552bf20521e18eab3d2d7a87cbb28f28268c))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 3.1.3 to 3.1.4. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v3.1.3...v3.1.4)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.10.7 to 1.10.8
  ([`d0b0322`](https://github.com/iwpnd/pyle38/commit/d0b032236873050065918d4c731195efcd38bb43))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.7 to 1.10.8. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.10.8/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.7...v1.10.8)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 4.5.4 to 4.5.5
  ([`85436c4`](https://github.com/iwpnd/pyle38/commit/85436c42a248498d2f1b469e05b990996b6b8d0c))

Bumps [redis](https://github.com/redis/redis-py) from 4.5.4 to 4.5.5. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.5.4...v4.5.5)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 3.1.1 to 3.1.3
  ([`f929be5`](https://github.com/iwpnd/pyle38/commit/f929be544f4279fe2682bc8483192f8085ca18af))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 3.1.1 to 3.1.3. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v3.1.1...v3.1.3)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.2.6 to 3.3.1
  ([`4a2f11f`](https://github.com/iwpnd/pyle38/commit/4a2f11f7eb0b193ce4bcd802230fed0b17fa678e))

Bumps [actions/cache](https://github.com/actions/cache) from 3.2.6 to 3.3.1. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.2.6...v3.3.1)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 4.5.3 to 4.5.4
  ([`7537c2a`](https://github.com/iwpnd/pyle38/commit/7537c2a1836f1bc835d697fb439c1c6151c9c79c))

Bumps [redis](https://github.com/redis/redis-py) from 4.5.3 to 4.5.4. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.5.3...v4.5.4)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.10.6 to 1.10.7
  ([`6a6ae95`](https://github.com/iwpnd/pyle38/commit/6a6ae95d3f3d0b3866b13f034122b0ca1594c531))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.6 to 1.10.7. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.10.7/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.6...v1.10.7)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- Fix link to blog
  ([`1023fe7`](https://github.com/iwpnd/pyle38/commit/1023fe7708d820eb3c53a9ec2c0785d811c8d25a))

- Update README.md
  ([`1dac812`](https://github.com/iwpnd/pyle38/commit/1dac8124a6cdae2bd168125a744e1275418b58ff))

closes #266

### Features

- ✨ bump pydantic to v2
  ([`6a1c557`](https://github.com/iwpnd/pyle38/commit/6a1c557965e52bf1bc2fda836a55e1fc4a4939a6))


## v0.9.1 (2023-03-24)

### Chores

- **deps**: Bump redis from 4.5.1 to 4.5.2
  ([`0435e57`](https://github.com/iwpnd/pyle38/commit/0435e57aa90d25d0c5e3992f25bc34a8fc5e7ead))

Bumps [redis](https://github.com/redis/redis-py) from 4.5.1 to 4.5.2. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.5.1...v4.5.2)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.10.5 to 1.10.6
  ([`76d85a4`](https://github.com/iwpnd/pyle38/commit/76d85a4eb0837ea6a138ef3c87d318f592b91ee2))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.5 to 1.10.6. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.10.6/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.5...v1.10.6)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.9.0 (2023-03-08)

### Bug Fixes

- 🐛 make client coroutine safe
  ([`6ab44c7`](https://github.com/iwpnd/pyle38/commit/6ab44c7b79ff9bd239d1b0c393d6da1286c3d110))

redis-py introduced locks on single connections in 4.5.0 to synchronize concurrency at the client
  level. However each individual connection is not coroutine safe.

to avoid issues here, Pyle38 will now use utilize Redis.execute_command instead of managing
  connections itself.

### Chores

- **deps**: Bump actions/cache from 3.2.4 to 3.2.6
  ([`e1ff316`](https://github.com/iwpnd/pyle38/commit/e1ff316211361626a42d1dc05be1d488607f81ed))

Bumps [actions/cache](https://github.com/actions/cache) from 3.2.4 to 3.2.6. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.2.4...v3.2.6)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 4.4.2 to 4.5.1
  ([`b51be64`](https://github.com/iwpnd/pyle38/commit/b51be6483c90ced1a356104491472bfe75ec02ca))

Bumps [redis](https://github.com/redis/redis-py) from 4.4.2 to 4.5.1. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.4.2...v4.5.1)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.10.4 to 1.10.5
  ([`ff7c7d1`](https://github.com/iwpnd/pyle38/commit/ff7c7d1e1f86d9202806444941b41f50dd5ebccf))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.4 to 1.10.5. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.10.5/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.4...v1.10.5)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.2.2 to 3.2.4
  ([`0823d40`](https://github.com/iwpnd/pyle38/commit/0823d40194a74c9671234d3cc4a85923914f5e04))

Bumps [actions/cache](https://github.com/actions/cache) from 3.2.2 to 3.2.4. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.2.2...v3.2.4)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Testing

- 🚨 fix tests and reset readonly option between tests
  ([`4f2c2b8`](https://github.com/iwpnd/pyle38/commit/4f2c2b816c2b261ce4fff793fcb1237806ef3ffd))


## v0.8.1 (2023-01-25)

### Bug Fixes

- 🐛 fset when field value is object
  ([`c16f487`](https://github.com/iwpnd/pyle38/commit/c16f4873948d2f1f4fc8be314ff268a6479b5b3b))

### Chores

- **deps**: Bump redis from 4.4.1 to 4.4.2
  ([`1a85ce4`](https://github.com/iwpnd/pyle38/commit/1a85ce489a27329463b03a850d7ec5e74a681172))

Bumps [redis](https://github.com/redis/redis-py) from 4.4.1 to 4.4.2. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.4.1...v4.4.2)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 4.4.0 to 4.4.1
  ([`1e1e267`](https://github.com/iwpnd/pyle38/commit/1e1e2679f73991c6d3a3d4bb75694085a92d305e))

Bumps [redis](https://github.com/redis/redis-py) from 4.4.0 to 4.4.1. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.4.0...v4.4.1)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.10.2 to 1.10.4
  ([`481eee7`](https://github.com/iwpnd/pyle38/commit/481eee7a1b9739ce3caa011dddec6b872791b2b9))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.10.2 to 1.10.4. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.10.4/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.10.2...v1.10.4)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.11 to 3.2.2
  ([`4d46ad4`](https://github.com/iwpnd/pyle38/commit/4d46ad4f7c31630fc8b3a6119dee1574678b8c3b))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.11 to 3.2.2. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.11...v3.2.2)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.8.0 (2022-12-22)

### Bug Fixes

- 🐛 rename to where_expr
  ([`8002e6a`](https://github.com/iwpnd/pyle38/commit/8002e6a627a95b1e7ddada7ca422bff7818d5484))

- 🐛 add whereable
  ([`1194a70`](https://github.com/iwpnd/pyle38/commit/1194a70ab21a82ac870a369abf22869822832312))

### Chores

- **deps**: Bump redis from 4.3.5 to 4.4.0
  ([`0978d8b`](https://github.com/iwpnd/pyle38/commit/0978d8bf1c30af1051f9323eed8a4b38b567df40))

Bumps [redis](https://github.com/redis/redis-py) from 4.3.5 to 4.4.0. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.3.5...v4.4.0)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump redis from 4.3.4 to 4.3.5
  ([`ac4e8c9`](https://github.com/iwpnd/pyle38/commit/ac4e8c91681b45cc8222bc47f4e3fb827a1757b9))

Bumps [redis](https://github.com/redis/redis-py) from 4.3.4 to 4.3.5. - [Release
  notes](https://github.com/redis/redis-py/releases) -
  [Changelog](https://github.com/redis/redis-py/blob/master/CHANGES) -
  [Commits](https://github.com/redis/redis-py/compare/v4.3.4...v4.3.5)

--- updated-dependencies: - dependency-name: redis dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.9 to 3.0.11
  ([`f98120d`](https://github.com/iwpnd/pyle38/commit/f98120d9d978937d089055ebece7ab90b03282c5))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.9 to 3.0.11. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.9...v3.0.11)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.8 to 3.0.9
  ([`ce5d95b`](https://github.com/iwpnd/pyle38/commit/ce5d95bf57eca493e0f02ea07b605c4e6f80867b))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.8 to 3.0.9. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.8...v3.0.9)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 3.1.0 to 3.1.1
  ([`0f1a06f`](https://github.com/iwpnd/pyle38/commit/0f1a06f337a05852a9d31015b50d25a8173bde1f))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 3.1.0 to 3.1.1. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v3.1.0...v3.1.1)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- Fix ([`d792507`](https://github.com/iwpnd/pyle38/commit/d792507be425151d9a63ef49af356143f499d519))

- 📚️ update readme
  ([`001f719`](https://github.com/iwpnd/pyle38/commit/001f719c7ab7c1240ec9a18a0afef1f956e2a22d))

### Features

- ✨ allow field Any field value
  ([`ddc3f4a`](https://github.com/iwpnd/pyle38/commit/ddc3f4a34807d801a3c98ed452e0bd355b641caf))

- ✨ add test helpers
  ([`277679b`](https://github.com/iwpnd/pyle38/commit/277679b65de53711fc4ee711ff4477562f23bd84))

- ✨ implement whereable
  ([`65fa065`](https://github.com/iwpnd/pyle38/commit/65fa0652d24c77dd02eeb9f1c1057a236d305fa2))

### Testing

- 🚨 update within tests with random data
  ([`01e24d5`](https://github.com/iwpnd/pyle38/commit/01e24d56debaae4034fe7b61e5fa8651e4c8c22a))

- 🚨 update sethook tests with random data
  ([`235a045`](https://github.com/iwpnd/pyle38/commit/235a045cc8e26a350ebd1a3f39a0be0baf01df4d))

- 🚨 update setchan tests with random data
  ([`eef77cf`](https://github.com/iwpnd/pyle38/commit/eef77cf1e3a53d1cdef7d799cbad5980c7fc2c74))

- 🚨 update search tests with random data
  ([`4865eca`](https://github.com/iwpnd/pyle38/commit/4865eca64f52e656926aefc3f420ebb9909551ba))

- 🚨 use test helper where possible
  ([`b8c5336`](https://github.com/iwpnd/pyle38/commit/b8c533683d19d0b179cca1e35ea99f1fc6d0c20b))

- 🚨 where with expression
  ([`24296a0`](https://github.com/iwpnd/pyle38/commit/24296a0606a2d2333d80219191b4470aed96168d))


## v0.7.0 (2022-09-06)

### Chores

- **deps**: Bump pydantic from 1.9.2 to 1.10.1
  ([`65c3657`](https://github.com/iwpnd/pyle38/commit/65c365772eac1e9019987de927e2bbfdf8378f20))

Bumps [pydantic](https://github.com/pydantic/pydantic) from 1.9.2 to 1.10.1. - [Release
  notes](https://github.com/pydantic/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/main/HISTORY.md) -
  [Commits](https://github.com/pydantic/pydantic/compare/v1.9.2...v1.10.1)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.5 to 3.0.8
  ([`79c216a`](https://github.com/iwpnd/pyle38/commit/79c216aacc90bf80b5def9e2db5c13ec3c09610c))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.5 to 3.0.8. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.5...v3.0.8)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.9.1 to 1.9.2
  ([`32d2f3f`](https://github.com/iwpnd/pyle38/commit/32d2f3f2854d4f1ef0555ef183d12eddf5b0c6bb))

Bumps [pydantic](https://github.com/samuelcolvin/pydantic) from 1.9.1 to 1.9.2. - [Release
  notes](https://github.com/samuelcolvin/pydantic/releases) -
  [Changelog](https://github.com/pydantic/pydantic/blob/v1.9.2/HISTORY.md) -
  [Commits](https://github.com/samuelcolvin/pydantic/compare/v1.9.1...v1.9.2)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.4 to 3.0.5
  ([`5c2ff67`](https://github.com/iwpnd/pyle38/commit/5c2ff6753577263611ac0c5126f9424c769337d5))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.4 to 3.0.5. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.4...v3.0.5)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/setup-python from 3 to 4
  ([`7ee2d20`](https://github.com/iwpnd/pyle38/commit/7ee2d20b4ac31cc6b45cad040bc8b4a139734c06))

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 3 to 4. - [Release
  notes](https://github.com/actions/setup-python/releases) -
  [Commits](https://github.com/actions/setup-python/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/setup-python dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.3 to 3.0.4
  ([`2cceffc`](https://github.com/iwpnd/pyle38/commit/2cceffcdcf3a8affce42f36e05304de0a8874db8))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.3 to 3.0.4. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.3...v3.0.4)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.2 to 3.0.3
  ([`f419ea9`](https://github.com/iwpnd/pyle38/commit/f419ea9b0cd8f98144ea174298ec4fa166eceea8))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.2 to 3.0.3. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.2...v3.0.3)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.9.0 to 1.9.1
  ([`ad23a58`](https://github.com/iwpnd/pyle38/commit/ad23a58481ff38877c1c8fb6f633b21e80838511))

Bumps [pydantic](https://github.com/samuelcolvin/pydantic) from 1.9.0 to 1.9.1. - [Release
  notes](https://github.com/samuelcolvin/pydantic/releases) -
  [Changelog](https://github.com/samuelcolvin/pydantic/blob/v1.9.1/HISTORY.md) -
  [Commits](https://github.com/samuelcolvin/pydantic/compare/v1.9.0...v1.9.1)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump github/codeql-action from 1 to 2
  ([`d1ca619`](https://github.com/iwpnd/pyle38/commit/d1ca619bd9ab27bcb9041ac8126dda747705e301))

Bumps [github/codeql-action](https://github.com/github/codeql-action) from 1 to 2. - [Release
  notes](https://github.com/github/codeql-action/releases) -
  [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/github/codeql-action/compare/v1...v2)

--- updated-dependencies: - dependency-name: github/codeql-action dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 2.1.0 to 3.1.0
  ([`2800a8c`](https://github.com/iwpnd/pyle38/commit/2800a8cda3cb22bff06605e3663fa2327eac07c4))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 2.1.0 to 3.1.0. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v2.1.0...v3.1.0)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 3.0.1 to 3.0.2
  ([`c136a19`](https://github.com/iwpnd/pyle38/commit/c136a19b4ed2ffc1d11d7c97781a77a464e4a687))

Bumps [actions/cache](https://github.com/actions/cache) from 3.0.1 to 3.0.2. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v3.0.1...v3.0.2)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/checkout from 2 to 3
  ([`c2b6c4a`](https://github.com/iwpnd/pyle38/commit/c2b6c4a9414e2677c287af9b4c482c0395227ebc))

Bumps [actions/checkout](https://github.com/actions/checkout) from 2 to 3. - [Release
  notes](https://github.com/actions/checkout/releases) -
  [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/actions/checkout/compare/v2...v3)

--- updated-dependencies: - dependency-name: actions/checkout dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 2.1.7 to 3.0.1
  ([`e2785dc`](https://github.com/iwpnd/pyle38/commit/e2785dcd9be241ff00a49c314c5a3848b024cfb2))

Bumps [actions/cache](https://github.com/actions/cache) from 2.1.7 to 3.0.1. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md) -
  [Commits](https://github.com/actions/cache/compare/v2.1.7...v3.0.1)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/setup-python from 2 to 3
  ([`33758d1`](https://github.com/iwpnd/pyle38/commit/33758d115ad6299d50f720fef57dc622f42bef3d))

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 2 to 3. - [Release
  notes](https://github.com/actions/setup-python/releases) -
  [Commits](https://github.com/actions/setup-python/compare/v2...v3)

--- updated-dependencies: - dependency-name: actions/setup-python dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

### Features

- ✨ upgrade to redis-py, use single connection instead of pool
  ([`b31136d`](https://github.com/iwpnd/pyle38/commit/b31136d0d18b9d78d6a286abaab0e2ba3b33f6c0))

chore: 🔧 lock file maintenance

### Testing

- 🚨 fix flaky follower tests
  ([`b95d212`](https://github.com/iwpnd/pyle38/commit/b95d212c0bbfdbf6eb697c7cf68a0d2738a5860a))

- 🚨 set asyncio-mode
  ([`72f5368`](https://github.com/iwpnd/pyle38/commit/72f5368e4fc7b74790a12b9b7edc4dea04ab1fb0))


## v0.6.1 (2022-01-24)

### Bug Fixes

- 🐛 generic types and defaults
  ([`45fcd5d`](https://github.com/iwpnd/pyle38/commit/45fcd5d6574242943d35ad5712403bbe1e70c81c))

### Documentation

- 📚️ new logo
  ([`d0c95d3`](https://github.com/iwpnd/pyle38/commit/d0c95d394dc584f2625e4c2c7206cd509ae3498f))


## v0.6.0 (2022-01-04)

### Chores

- **deps**: Bump pydantic from 1.8.2 to 1.9.0
  ([`d4ec8da`](https://github.com/iwpnd/pyle38/commit/d4ec8da7d95c301dd72e9be7cdeeb55ff0f14dc7))

Bumps [pydantic](https://github.com/samuelcolvin/pydantic) from 1.8.2 to 1.9.0. - [Release
  notes](https://github.com/samuelcolvin/pydantic/releases) -
  [Changelog](https://github.com/samuelcolvin/pydantic/blob/master/HISTORY.md) -
  [Commits](https://github.com/samuelcolvin/pydantic/compare/v1.8.2...v1.9.0)

--- updated-dependencies: - dependency-name: pydantic dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from 2.1.6 to 2.1.7
  ([`01acdaf`](https://github.com/iwpnd/pyle38/commit/01acdaf7e7d2c11d79a251616703d2cca818c74f))

Bumps [actions/cache](https://github.com/actions/cache) from 2.1.6 to 2.1.7. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Commits](https://github.com/actions/cache/compare/v2.1.6...v2.1.7)

--- updated-dependencies: - dependency-name: actions/cache dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump snok/install-poetry from 1.2 to 1.3
  ([`2912a12`](https://github.com/iwpnd/pyle38/commit/2912a1296cdd386fc9116cff55d002f24fef5035))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.2 to 1.3. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.2...v1.3)

--- updated-dependencies: - dependency-name: snok/install-poetry dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- 📚️ update readme
  ([`4b57fbf`](https://github.com/iwpnd/pyle38/commit/4b57fbfadd5e7bb89797801f8e516f317effaa19))

### Features

- ✨ add buffer search option to within search
  ([`1ad3655`](https://github.com/iwpnd/pyle38/commit/1ad3655c022b67f6b1a33928219641818974e152))

- ✨ add buffer search option to intersects search
  ([`f23d800`](https://github.com/iwpnd/pyle38/commit/f23d8002b3fcefef242d0cd1ec8bbaec656fef15))


## v0.5.1 (2021-11-21)

### Bug Fixes

- 🐛 remove stringobject class in favour of generics
  ([`8317d40`](https://github.com/iwpnd/pyle38/commit/8317d40420b4625ea2b95b392da49177e817a1ef))

- 🐛 utilize generic model object
  ([`1f95d2c`](https://github.com/iwpnd/pyle38/commit/1f95d2c6d9adb06871749468991c9f38c5d5d6eb))

- 🐛 get as string object
  ([`9f1a3a3`](https://github.com/iwpnd/pyle38/commit/9f1a3a3eb17a196538938d9c6cb27a19b3fe18eb))

### Documentation

- 📚️ update docs
  ([`04cad31`](https://github.com/iwpnd/pyle38/commit/04cad3155a9b103eef8f121f6d10a1910d796260))


## v0.5.0 (2021-10-04)

### Chores

- **deps**: Bump snok/install-poetry from 1.1.8 to 1.2
  ([`069f5ca`](https://github.com/iwpnd/pyle38/commit/069f5ca6061b7acafc598e886512cbe76520ec0d))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.1.8 to 1.2. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.1.8...v1.2)

--- updated-dependencies: - dependency-name: snok/install-poetry dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 2.0.3 to 2.1.0
  ([`1988a36`](https://github.com/iwpnd/pyle38/commit/1988a36bf2da6d587cdd2ff3cd36ec6db51013b6))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 2.0.3 to 2.1.0. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v2.0.3...v2.1.0)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

### Features

- ✨ add sector search to within and intersects
  ([`4b6931b`](https://github.com/iwpnd/pyle38/commit/4b6931ba59d9c4a573a7e54452b74bc640cac0e1))


## v0.4.0 (2021-09-10)

### Bug Fixes

- 🐛 update server extended response
  ([`62628fb`](https://github.com/iwpnd/pyle38/commit/62628fb14b0444a381fe2da3b59e384ad39460de))

### Chores

- **deps**: Bump snok/install-poetry from 1.1.7 to 1.1.8
  ([`e67a9c2`](https://github.com/iwpnd/pyle38/commit/e67a9c2637dfc98a37be11523ec5d3b6b4328ee4))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.1.7 to 1.1.8. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.1.7...v1.1.8)

--- updated-dependencies: - dependency-name: snok/install-poetry dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 2.0.2 to 2.0.3
  ([`4bb84bd`](https://github.com/iwpnd/pyle38/commit/4bb84bd8ed72b569907b1301d26bf1b261a0de5b))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 2.0.2 to 2.0.3. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v2.0.2...v2.0.3)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump codecov/codecov-action from 1 to 2.0.2
  ([`52848ac`](https://github.com/iwpnd/pyle38/commit/52848acf0e8b579463b6a107b44bb4c9a46132c5))

Bumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 1 to 2.0.2. -
  [Release notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v1...v2.0.2)

--- updated-dependencies: - dependency-name: codecov/codecov-action dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump snok/install-poetry from 1.1.6 to 1.1.7
  ([`77e2a3f`](https://github.com/iwpnd/pyle38/commit/77e2a3f62f2afbaa1848639908b0b7ac622080c5))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.1.6 to 1.1.7. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.1.6...v1.1.7)

--- updated-dependencies: - dependency-name: snok/install-poetry dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- 📚️ update docs
  ([`8a7cec2`](https://github.com/iwpnd/pyle38/commit/8a7cec286ee472361a7c2e1c7ec8c974f4a8ae71))

- 📚️ update docs
  ([`4fcc6e6`](https://github.com/iwpnd/pyle38/commit/4fcc6e664fc229d68465a0cca34e9ae4c48ddd62))

- Update readme, fix typo
  ([`e4a02f2`](https://github.com/iwpnd/pyle38/commit/e4a02f2c21d651d8b7bc4aa19cfaeef1ead87898))

- 📚️ update readme
  ([`d318051`](https://github.com/iwpnd/pyle38/commit/d3180518c799897c8c0f65af80c669bc04c89f90))

- 📚️ update docs, add logo
  ([`09b44e2`](https://github.com/iwpnd/pyle38/commit/09b44e2071d79d26ed04faa1b26d53625ea15f82))

### Features

- ✨ add where filter to scan command
  ([`8c78d8b`](https://github.com/iwpnd/pyle38/commit/8c78d8b54ba4554b433334f98eaaf00110fe3b99))

- ✨ add where filter to search command
  ([`5e02bd4`](https://github.com/iwpnd/pyle38/commit/5e02bd40711021a09bb1db6c6ece561af707ecd8))

- ✨ add where filter to nearby command
  ([`0f795c8`](https://github.com/iwpnd/pyle38/commit/0f795c878ff8c84d41a712643ae773aba25b7b04))

- ✨ add where filter to intersects command
  ([`dbf8be1`](https://github.com/iwpnd/pyle38/commit/dbf8be14697f2f422e462e90140b66ce17a5a7c3))

- ✨ add where filter to within command
  ([`ceb5a29`](https://github.com/iwpnd/pyle38/commit/ceb5a29aad148c96729da8b2879fbec6a5d30605))

### Testing

- 🚨 remove get to follower, flaky
  ([`f102b8d`](https://github.com/iwpnd/pyle38/commit/f102b8da91a92f46cd67c703f1e3b03859cedf2e))

- 🚨 remove flaky tests leader<>follower
  ([`4ef1d64`](https://github.com/iwpnd/pyle38/commit/4ef1d64fc2f2ee7a4c010554220ccc3210f870f4))


## v0.3.2 (2021-07-31)


## v0.3.1 (2021-07-25)

### Bug Fixes

- 🐛 redis from url is sync
  ([`7842e76`](https://github.com/iwpnd/pyle38/commit/7842e76a9bd870709030a4d5779d22d4faa18f0d))

### Documentation

- 📚️ remove duplicated changelog entries [skip ci]
  ([`9743221`](https://github.com/iwpnd/pyle38/commit/9743221c33282b9fc8206275f6cc3a6922efa886))

### Testing

- 🚨 increase delay between leader and follower further
  ([`2b63afc`](https://github.com/iwpnd/pyle38/commit/2b63afc93ff61701b2db3ca848ffa5e4b418e58d))


## v0.3.0 (2021-06-27)

### Bug Fixes

- 🐛 incompatible return types on subclass follower
  ([`600e59f`](https://github.com/iwpnd/pyle38/commit/600e59f915c39d59a57c5d17570e29a5c24d7807))

### Features

- ✨ add INFO command
  ([`3e3d916`](https://github.com/iwpnd/pyle38/commit/3e3d9160d0f8dbc6409beab373234f0e6009683a))

### Testing

- 🚨 increase delay between leader follower in ci
  ([`ec4afa7`](https://github.com/iwpnd/pyle38/commit/ec4afa7f0aebf64a5805ef0139067ee8fe834dd2))

- 🚨 sleep between set/get for follower tests
  ([`780df65`](https://github.com/iwpnd/pyle38/commit/780df65360f94b00342a39afdef799f482e3fc62))


## v0.2.0 (2021-06-12)

### Chores

- **deps**: Bump actions/cache from 2.1.5 to 2.1.6
  ([`71d452c`](https://github.com/iwpnd/pyle38/commit/71d452c61b0686b270712695122c195cb14574b9))

Bumps [actions/cache](https://github.com/actions/cache) from 2.1.5 to 2.1.6. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Commits](https://github.com/actions/cache/compare/v2.1.5...v2.1.6)

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump snok/install-poetry from 1.1.4 to 1.1.6
  ([`2b3d362`](https://github.com/iwpnd/pyle38/commit/2b3d36295b92c95934da7e488e31228bf89b3da4))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from 1.1.4 to 1.1.6. - [Release
  notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.1.4...v1.1.6)

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pydantic from 1.8.1 to 1.8.2
  ([`2bef2c2`](https://github.com/iwpnd/pyle38/commit/2bef2c21e717516a2cb4e7c15d1fa1a174087495))

Bumps [pydantic](https://github.com/samuelcolvin/pydantic) from 1.8.1 to 1.8.2. - [Release
  notes](https://github.com/samuelcolvin/pydantic/releases) -
  [Changelog](https://github.com/samuelcolvin/pydantic/blob/master/HISTORY.md) -
  [Commits](https://github.com/samuelcolvin/pydantic/compare/v1.8.1...v1.8.2)

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/cache from v2.1.4 to v2.1.5
  ([`88bf8b2`](https://github.com/iwpnd/pyle38/commit/88bf8b2a02c9b20acb12efc4d228d023717242e6))

Bumps [actions/cache](https://github.com/actions/cache) from v2.1.4 to v2.1.5. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Commits](https://github.com/actions/cache/compare/v2.1.4...1a9e2138d905efd099035b49d8b7a3888c653ca8)

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump snok/install-poetry from v1.1.2 to v1.1.4
  ([`220f86a`](https://github.com/iwpnd/pyle38/commit/220f86aa21cc5ea476723cfd4f762138bbe42045))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from v1.1.2 to v1.1.4. -
  [Release notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.1.2...fe3362f94a7d193ecae442ec43e79680358051ce)

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- 📚️ fix toc
  ([`c6ec31c`](https://github.com/iwpnd/pyle38/commit/c6ec31cc35d618b1af90fdc796219907a0af2b3b))

- 📚️ update readme
  ([`b79519b`](https://github.com/iwpnd/pyle38/commit/b79519b1c9f40cd3172147ddb723a4244ee5e9bb))

- 📚️ add docstrings to commands/nearby
  ([`b2da4e2`](https://github.com/iwpnd/pyle38/commit/b2da4e2732aa44e00e65c7ebff31c27d4f7f7f42))

- 📚️ add docstrings to commands/intersects
  ([`4a60046`](https://github.com/iwpnd/pyle38/commit/4a60046c99cdb4b21670ea051b18fcca1c27d88f))

- 📚️ add docstrings to commands/within
  ([`40f68c3`](https://github.com/iwpnd/pyle38/commit/40f68c3817d7527addb44a53a0af19e500f12d21))

- Fix typo
  ([`dec5454`](https://github.com/iwpnd/pyle38/commit/dec54541f871d80f050c039beffbe306ea79998e))

- Update readme with local infra setup [skip ci]
  ([`a794627`](https://github.com/iwpnd/pyle38/commit/a7946273b040538320ecb7d2cfd7a0a68ff3d685))

### Features

- ✨ add HEALTHZ command
  ([`3af13b4`](https://github.com/iwpnd/pyle38/commit/3af13b42dd0a773c1f22122b7a267bd80221d7f9))

### Refactoring

- ♻️ bind TypeVar T to dict specifically
  ([`a750c25`](https://github.com/iwpnd/pyle38/commit/a750c25805515c4e56f5e745dc087299b4ea537d))

### Testing

- 🚨 add sleep between leader follower interactions
  ([`940bbed`](https://github.com/iwpnd/pyle38/commit/940bbed9efcc1fcb1079fda07b1d782d0dd9e200))

- 🚨 fix flaky test involving follower to be caught up
  ([`186446e`](https://github.com/iwpnd/pyle38/commit/186446e574cbd16ab9390c4ebbf953022a707c2d))


## v0.1.0 (2021-04-08)

### Bug Fixes

- Import Tile38 from root
  ([`9e0a8e8`](https://github.com/iwpnd/pyle38/commit/9e0a8e8e961b4e4e26b62f515391a60808a3cfa9))

- Mypy issues, add pytest coverage
  ([`07c395d`](https://github.com/iwpnd/pyle38/commit/07c395d48619cf04ea4ebcf9bb3bc0b335fff5d5))

- Reset options on init
  ([`1ea2954`](https://github.com/iwpnd/pyle38/commit/1ea295459540b0d049a70b7f81bf945fb408de95))

- Command stats and response
  ([`06e4df6`](https://github.com/iwpnd/pyle38/commit/06e4df6929b0fca0e9963be50b702e662082d211))

- Add poethepoet and fix mypy errors
  ([`02a0aef`](https://github.com/iwpnd/pyle38/commit/02a0aef367eaaec3b1c20da3040c09fc1e1ba9ea))

- Redis connection pool
  ([`87967cc`](https://github.com/iwpnd/pyle38/commit/87967cc0fc3b1732e4d32b8173f587ca11083193))

### Chores

- **deps**: Bump actions/cache from v2 to v2.1.4
  ([`88a92b7`](https://github.com/iwpnd/pyle38/commit/88a92b7bbe3eb09db7360d4a3b7f560044f36394))

Bumps [actions/cache](https://github.com/actions/cache) from v2 to v2.1.4. - [Release
  notes](https://github.com/actions/cache/releases) -
  [Commits](https://github.com/actions/cache/compare/v2...26968a09c0ea4f3e233fdddbafd1166051a095f6)

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump snok/install-poetry from v1.0.0 to v1.1.2
  ([`314bdb1`](https://github.com/iwpnd/pyle38/commit/314bdb1c19301b8b210c6ed05f4db7e51f917230))

Bumps [snok/install-poetry](https://github.com/snok/install-poetry) from v1.0.0 to v1.1.2. -
  [Release notes](https://github.com/snok/install-poetry/releases) -
  [Commits](https://github.com/snok/install-poetry/compare/v1.0.0...b67da837e42fb77252a06a3eb84cf0ccaad73aa9)

Signed-off-by: dependabot[bot] <support@github.com>

### Documentation

- Fix typo, add classifiers
  ([`b1a0f54`](https://github.com/iwpnd/pyle38/commit/b1a0f5421500cb1ce4e6835ab1fa8a4292c15685))

- Add ipython example [skip ci]
  ([`94eafa5`](https://github.com/iwpnd/pyle38/commit/94eafa533ffaf225fc2bf83a9d55848c3ad80e1d))

- Fix sethook / setchan docs [skip ci]
  ([`2358896`](https://github.com/iwpnd/pyle38/commit/2358896c7defb4ab6384b330063104fc30984c10))

- Minimum viable example to readme
  ([`51988be`](https://github.com/iwpnd/pyle38/commit/51988be644ee78910356487261cef7edce56390e))

- Add readme
  ([`4ab148f`](https://github.com/iwpnd/pyle38/commit/4ab148ff3892511e57a78f7cd751044d186dd1b8))

### Features

- Add command fset
  ([`510743a`](https://github.com/iwpnd/pyle38/commit/510743aab1227152a4ef35c7e9717c53d4592946))

- Add command setchan
  ([`d15bc25`](https://github.com/iwpnd/pyle38/commit/d15bc2534d7114f0a6660585d8a15ca890c84aec))

- Add command sethook
  ([`a125da2`](https://github.com/iwpnd/pyle38/commit/a125da2cf6d383af77926443234d1732366d50d7))

- Use fields in responses correctly, fix pointsresponse
  ([`3efbb1b`](https://github.com/iwpnd/pyle38/commit/3efbb1be3be5e66556f4cd1eca8a65afdf6737c6))

- Add fields to command set
  ([`31cdd2f`](https://github.com/iwpnd/pyle38/commit/31cdd2f1d5a9ae027af97dba9dc4005c39f7c7d8))

- Add command search
  ([`ea1c98f`](https://github.com/iwpnd/pyle38/commit/ea1c98fa110180f0cdca53b6764b5882364cc1b2))

- Add command scan
  ([`929c839`](https://github.com/iwpnd/pyle38/commit/929c839df87a86993d548569ea6744a4593ad61e))

- Add command nearby
  ([`3681118`](https://github.com/iwpnd/pyle38/commit/3681118e3d2d0c0caa92e5cc03f06e0d336ac2a5))

- Add command within
  ([`b8f7713`](https://github.com/iwpnd/pyle38/commit/b8f771396be46577a04d55a8b9088b0999083fbf))

- Add command intersects, fix mypy issues, move queries to models
  ([`aa3806e`](https://github.com/iwpnd/pyle38/commit/aa3806ed26f3aa528f81b4cfbfb366d475fdcf79))

- Add command drop
  ([`2454033`](https://github.com/iwpnd/pyle38/commit/2454033776a143d582ffe3c6462d6f11d216cdc6))

- Add setchan delchan pdelchan sethook delhook pdelhook and delete
  ([`55905ec`](https://github.com/iwpnd/pyle38/commit/55905ec19dab94ea22a6bf97c7b2461f886a2a83))

- Add command rename renamenx
  ([`88e9427`](https://github.com/iwpnd/pyle38/commit/88e94278ad482ca2e5c17081e3df0869a332924b))

- Add command readonly
  ([`679856c`](https://github.com/iwpnd/pyle38/commit/679856ca72ab2d9b6dac0b5ee5eb356043ab05fb))

- Add command persist expire ttl
  ([`18b071e`](https://github.com/iwpnd/pyle38/commit/18b071e2f6b053bab2debd627d88369cf4804ede))

- Add pdel command, override exec in command set
  ([`32266f3`](https://github.com/iwpnd/pyle38/commit/32266f3bcebbf394a3ee6703c172554f7da7827c))

- Add command stats
  ([`e759586`](https://github.com/iwpnd/pyle38/commit/e7595868fda20c89a2c53857e3703699f2c05151))

- Add command server extended
  ([`5cc44b8`](https://github.com/iwpnd/pyle38/commit/5cc44b8ec8ba304679f1cc80b70baa4818c55100))

- Add commands keys ping and server
  ([`220ba0d`](https://github.com/iwpnd/pyle38/commit/220ba0d4e47cb7f802c51f00a7080d548680f86a))

- Add JSET/JGET/JDEL
  ([`10f0068`](https://github.com/iwpnd/pyle38/commit/10f0068b85bdb31cd2861f5a3949f62e703b1b17))

- Add hooks command
  ([`1a3d8b9`](https://github.com/iwpnd/pyle38/commit/1a3d8b938049042760d8686e7bd224dea24394e2))

- Add gc
  ([`4c60d8f`](https://github.com/iwpnd/pyle38/commit/4c60d8fcfccd3f742786e7effa31f00174fec45a))

- Add config set get rewrite
  ([`9b846c6`](https://github.com/iwpnd/pyle38/commit/9b846c675d12d2c0dd451c057fa27a48b04cbf6f))

- Add responses to Get
  ([`33f680a`](https://github.com/iwpnd/pyle38/commit/33f680aa51aca6b0439065d3a299345d49acedf4))

- Add response classes, sort imports
  ([`7e28aee`](https://github.com/iwpnd/pyle38/commit/7e28aee24ef5b1f20c59f75bc3dc35d6ebda2560))

- Add leader, follower and tile38. add set/get commands
  ([`9533631`](https://github.com/iwpnd/pyle38/commit/9533631adadef49b0733aa319f8ddd5b85212123))

- Initial commit 🎉
  ([`bc10d18`](https://github.com/iwpnd/pyle38/commit/bc10d189e34dfb443a45404809d2eb1902016f9b))

### Refactoring

- Remove redundant withclient
  ([`5860ef9`](https://github.com/iwpnd/pyle38/commit/5860ef956b200cb30dd132d260a46882c5f6519a))

- Id is always string as tile38 coerces int to str anyways
  ([`5661adf`](https://github.com/iwpnd/pyle38/commit/5661adf76df52a3dfa1cf2d6ff11e6e3aa477324))

- Return json response if Command.SET instead of dict
  ([`e2b30b1`](https://github.com/iwpnd/pyle38/commit/e2b30b15a61ad808da8faa61942f2067ef9aaac5))

- No tile38 url set exception handling and consistent naming
  ([`a1874e6`](https://github.com/iwpnd/pyle38/commit/a1874e6e32d7bf9ad0f303b785abd227845384a7))

- Make private, refactor tests to use follower also
  ([`d57bb77`](https://github.com/iwpnd/pyle38/commit/d57bb7772d337d360ae1cf3764ff1347d85b7a1e))

- Parametrize tests, renaming for consistency
  ([`2a1570e`](https://github.com/iwpnd/pyle38/commit/2a1570ed79c0c1acc68adfce09c87afc153dfb39))

### Testing

- Add test for intersecting polygons
  ([`b2616ee`](https://github.com/iwpnd/pyle38/commit/b2616ee028ecb037e52500b01812b1145ab06d5c))

- Add conftest to handle tile38 connection and teardown/flushdb
  ([`e69aef9`](https://github.com/iwpnd/pyle38/commit/e69aef9ae7d1b0b8a9da20bb68e4db3717c77d06))
