# Databricks Asset Bundles for Spark Connect Rust

Get started with the template by cloning this repo and running the following command

```
databricks bundle init PATH_TO_CHECKOUT
```

Or use this template directly with the following command 

```
databricks bundle init git@github.com:sjrusso8/dab-template-rust-unofficial.git
```

## Background

This template is an example of how to use [spark-connect-rs](https://github.com/sjrusso8/spark-connect-rs) 
with a databricks asset bundle. This template works for regular job clusters, and 
serverless job clusters. 

## Dependencies

1. [Databricks CLI](https://docs.databricks.com/dev-tools/cli/databricks-cli.html)

2. [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) (duh)

2. [uv](https://docs.astral.sh/uv/getting-started/installation/) as the package and project manager 

3. [maturin](https://www.maturin.rs/installation) to build rust binaries as python packages

## Refs

1. [Databricks Asset Bundle: default-python](https://github.com/databricks/cli/tree/main/libs/template/templates/default-python)
2. [dab-template-goland-unofficial](https://github.com/grundprinzip/dab-template-golang-unofficial)
