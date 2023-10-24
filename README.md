# pgstac-ingestor

An API for large scale STAC data ingestion and validation into a pgSTAC instance.

![ingestor](https://github.com/developmentseed/pgstac-ingestor/assets/10407788/8176573a-1242-4897-8cdc-3fba2e4b2dc1)

Authentication for the STAC Ingestor API can be configured with JWTs authenticated by JWKS.  To learn more about securing FastAPI applications with this approach see [Securing FastAPI with JWKS (AWS Cognito, Auth0)](https://alukach.com/posts/fastapi-rs256-jwt/).

A sample Cognito-based authentication system is available at [aws-asdi-auth](https://github.com/developmentseed/aws-asdi-auth).

---

**Documentation**: <a href="https://developmentseed.org/pgstac-ingestor/" target="_blank">https://developmentseed.org/pgstac-ingestor/</a>

**Source Code**: <a href="https://github.com/developmentseed/pgstac-ingestor" target="_blank">https://github.com/developmentseed/pgstac-ingestor</a>

---

## Install

```bash
$ python -m pip install -U pip
$ python -m pip install pgstac-ingestor

# Or install from source:
$ python -m pip install -U pip
$ python -m pip install git+https://github.com/developmentseed/pgstac-ingestor.git
```

## Changes

See [CHANGES.md](https://github.com/developmentseed/pgstac-ingestor/blob/main/CHANGES.md).

## Contribution & Development

See [CONTRIBUTING.md](https://github.com/developmentseed/pgstac-ingestor/blob/main/CONTRIBUTING.md)

## License

See [LICENSE](https://github.com/developmentseed/pgstac-ingestor/blob/main/LICENSE)

## Authors

Created by [Development Seed](<http://developmentseed.org>)
