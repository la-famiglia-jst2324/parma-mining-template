# parma-mining-template

ParmaAI copier template for data mining sub-services.


## Getting Started

The following steps will get you started with the project.

1. Pre-requisites: to be able to create a new submodule using this template, make sure to comply with the following prerequisites.

   - Configure GitHub via an ssh key. Key based authenticated is highly encouraged. See [GitHub Docs](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) for more information.
   - Please make sure to have an GPG key configured for GitHub. See [GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account) for more information.
   - Install **micromamba**, a conda environment management package manager, as described [here](https://mamba.readthedocs.io/en/latest/micromamba-installation.html). Alternatively conda or mamba installations should also work, but are highly discouraged because of their slow performance.
   - Install **pre-commit**, See [pre-commit installation](https://pre-commit.com/#install)


## Usage

To create a new data mining module, follow below steps:

1. Create a new GitHub repository.

Repository name should be in format **parma-mining-<module_name>**

2. Clone the repository locally and open (cd) it.

3. Activate any **micromamba environment** with **copier** installed.

   1. If you have a micromamba environment with copier installed, you can activate it. 
       ```bash
       micromamba activate <env name>
       ```

   2. Otherwise, you can create a new one and activate it. After you create an environment for the first time, you can reuse it next time.
    ```bash
    micromamba create -n copier-env -c conda-forge # create a new environment named copier-env
    micromamba activate copier-env # activate the environment
    micromamba install copier -c conda-forge # install copier
    ```

4. Run copier

    ```bash
    copier copy git@github.com:la-famiglia-jst2324/parma-mining-template.git . --trust
    ```

   1. Optional: Update project with a new copier template version.

       ```bash
       copier update --trust
       ```
5. Deactivate the environment

    ```bash
    micromamba deactivate
    ```