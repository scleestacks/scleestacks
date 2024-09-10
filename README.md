# SCleeStacks

## Overview

This project is an effort to establish a unified containerization strategy for the [scverse](https://scverse.org/) ecosystem. Beyond individual tool containerization, efforts have been made to assemble multi-tool images around commonly used workflows and integrations.

## User Guide

### Accessing the Container Registry

1. Container images are hosted on GitHub Container Registry (ghcr.io/scleestacks). The catalogue of available images can be found in the [SCleeStacks packages](https://github.com/orgs/scleestacks/packages) section.

2. To access the registry, you'll need to authenticate with GitHub. You can do this using your GitHub credentials or a personal access token.

### Available Images

Our registry contains two types of images:

1. **Individual Tools**: Separate images for each tool from the scverse ecosystem. Package releases capture for containerization begin with versions current as of June 2024.
2. **Stacks**: Integrated images containing multiple tools commonly used together.
    - airr-multi (scirpy, muon, scanpy)
    - scvi-cpu-base (scvi-tools, scanpy)
    - scvi-cpu-multi (scvi-tools, muon, scanpy)
    - scvi-gpu-base (cuda, scvi-tools, scanpy) *very large*
    - scvi-gpu-multi (cuda, scvi-tools, muon, scanpy) *very large*
    - spatial-base (scanpy, spatialdata, squidpy)

### Pulling Images

To pull an image from our registry, use the following command:

```bash
docker pull ghcr.io/scleestacks[image-name]:[tag]
```

Replace ```[image-name]```, and ```[tag]``` with the appropriate values.

### Using Images

#### devcontainers

#### Multi-container Orchestration

## Contributor Guide

We welcome contributions to our container registry project. Much of the basis for this work depends on community consensus for stadardization, so please feel free to weigh in whether you are a maintainer or user of scverse tools.

### Contributing Process

1. **Fork the Repository**: Start by forking the main repository to your GitHub account.

2. **Clone Your Fork**: Clone your forked repository to your local machine.

3. **Create a Branch**: Create a new branch for your contribution.

4. **Make Changes**: Implement your changes, whether it's adding a new image, updating an existing one, or modifying documentation.

5. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message.

6. **Push to Your Fork**: Push your changes to your forked repository.

7. **Create a Pull Request**: Go to the original repository on GitHub and create a new pull request from your feature branch.

### Creating and Updating Images

#### Dockerfile Guidelines

- Follow best practices for writing Dockerfiles
    - Minimize layers
    - Establish deterministic builds in all possible cases
    - Start with lean base images. Current base image defaults:
        - CPU: python:3.10-slim
        - GPU: nvidia/cuda:12.1.0-devel-ubuntu22.04
- Include necessary metadata (maintainer, version information, etc.).
- Place your Dockerfile in the appropriate directory within the repository.

#### GitHub Actions Workflow

We use GitHub Actions to automatically build and publish images. To set up a workflow for your image:

1. Create a new `.yml` file in the `.github/workflows/` directory of the repository.
2. Use the `workflow-template.yml` located in the templates directory as a starting point. Replace the env and name vars in square brackets with the appropriate values.
3. Customize the workflow as needed for your specific image or stack.
4. Stack workflow file names should be prefixed with "zz-" to help with organization.

### Creating Stacks

To create a new stack (an integrated image of multiple tools):

1. Create a new Dockerfile that includes all necessary tools.
2. Use multi-stage builds, isolation of individual tool dependencies, and pip-based reconciliation.
3. Ensure your stack image is well-documented, explaining which tools are included and how to use them together.

### Testing

- Include appropriate tests for your images in the repository.
- Ensure your workflow includes steps to run these tests before pushing the image.

### Documentation

- Update the main README.md file if you're adding new features or changing existing ones.
- Provide clear usage instructions for any new images or stacks you create.

### Troubleshooting

If you encounter issues while contributing, please check our [Issues](https://github.com/scleestacks/scleestacks/issues) page for known problems and solutions. If your issue isn't addressed, feel free to open a new issue.

## Best Practices

- Always tag your images with specific versions to ensure reproducibility.
- Include detailed metadata for stacks in your Dockerfiles and in-place using the `generate-stack-metadata.sh` script.
- Regularly update base images to include security patches.
- Write clear and concise commit messages and pull request descriptions.
- Engage in respectful and constructive communication in issues and pull requests.
