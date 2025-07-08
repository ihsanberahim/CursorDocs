# Combined Documentation for n8n
<!-- Source .knowledge file: n8n/.knowledge -->
<!-- GitHub API Roots: https://api.github.com/repos/n8n-io/n8n-docs/contents/docs -->



---

<!-- Source: docs/1-0-migration-checklist.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n v1.0 migration guide
description: What's new in version 1
contentType: reference
---

# n8n v1.0 migration guide

This document provides a summary of what you should be aware of before updating to version 1.0 of n8n.

The release of n8n 1.0 marks a milestone in n8n's journey to make n8n available for demanding production environments. Version 1.0 represents the hard work invested over the last four years to make n8n the most accessible, powerful, and versatile automation tool. n8n 1.0 is now ready for use in production.

## New features

### Python support in the Code node

Although JavaScript remains the default language, you can now also select Python as an option in the [Code node](/code/code-node.md) and even make use of [many Python modules](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide){:target=_blank .external link}. Note that Python is unavailable in Code nodes added to a workflow before v1.0.

[PR #4295](https://github.com/n8n-io/n8n/pull/4295){:target=_blank .external link}, [PR #6209](https://github.com/n8n-io/n8n/pull/6209){:target=_blank .external link}

### Execution order

n8n 1.0 introduces a new execution order for multi-branch workflows:

In multi-branch workflows, n8n needs to determine the order in which to execute nodes on branches. Previously, n8n executed the first node of each branch, then the second of each branch, and so on (breadth-first). The new execution order ensures that each branch executes completely before starting the next one (depth-first). Branches execute based on their position on the canvas, from top to bottom. If two branches are at the same height, the leftmost one executes first.

n8n used to execute multi-input nodes as long as they received data on their first input. Nodes connected to the second input of multi-input nodes automatically executed regardless of whether they received data. The new execution order introduced in n8n 1.0 simplifies this behavior: Nodes are now executed only when they receive data, and multi-input nodes require data on at least one of their inputs to execute.

Your existing workflows will use the legacy order, while new workflows will execute using the v1 order. You can configure the execution order for each workflow in [workflow settings](/workflows/settings.md).

[PR #4238](https://github.com/n8n-io/n8n/pull/4238){:target=_blank .external link}, [PR #6246](https://github.com/n8n-io/n8n/pull/6246){:target=_blank .external link}, [PR #6507](https://github.com/n8n-io/n8n/pull/6507){:target=_blank .external link}

## Deprecations

### MySQL and MariaDB

n8n has removed support for MySQL and MariaDB as storage backends for n8n. These database systems are used by only a few users, yet they require continuous development and maintenance efforts. n8n recommends migrating to PostgreSQL for better compatibility and long-term support.

[PR #6189](https://github.com/n8n-io/n8n/pull/6189){:target=_blank .external link}

### EXECUTIONS_PROCESS and "own" mode

Previously, you could use the `EXECUTIONS_PROCESS` environment variable to specify whether executions should run in the `main` process or in their `own` processes. This option and `own` mode are now deprecated and will be removed in a future version of n8n. This is because it led to increased code complexity while offering marginal benefits. Starting from n8n 1.0, `main` will be the new default.

Note that executions start much faster in `main` mode than in `own` mode. However, if a workflow consumes more memory than is available, it might crash the entire n8n application instead of just the worker thread. To mitigate this, make sure to allocate enough system resources or configure [queue mode](/hosting/scaling/queue-mode.md) to distribute executions among multiple workers.

[PR #6196](https://github.com/n8n-io/n8n/pull/6196){:target=_blank .external link}

## Breaking changes

### Docker

#### Permissions change

When using Docker-based deployments, the n8n process is now run by the user `node` instead of `root`. This change increases security.

If permission errors appear in your n8n container logs when starting n8n, you may need to update the permissions by executing the following command on the Docker host:

```bash
docker run --rm -it --user root -v ~/.n8n:/home/node/.n8n --entrypoint chown n8nio/base:16 -R node:node /home/node/.n8n
```

#### Image removal

We've removed the Debian and RHEL images. If you were using these you need to change the image you use. This shouldn't result in any errors unless you were making a custom image based on one of those images.

#### Entrypoint change

The entrypoint for the container has changed and you no longer need to specify the n8n command. If you were previously running `n8n worker --concurrency=5` it's now `worker --concurrency=5`

[PR #6365](https://github.com/n8n-io/n8n/pull/6365){:target=_blank .external link}

### Workflow failures due to expression errors

Workflow executions may fail due to syntax or runtime errors in expressions, such as those that reference non-existent nodes. While expressions already throw errors on the frontend, this change ensures that n8n also throws errors on the backend, where they were previously silently ignored. To receive notifications of failing workflows, n8n recommends setting up an "error workflow" under workflow settings.

[PR #6352](https://github.com/n8n-io/n8n/pull/6352){:target=_blank .external link}

### Mandatory owner account

This change makes [User Management](/user-management/index.md) mandatory and removes support for other authentication methods, such as BasicAuth and External JWT. Note that the number of permitted users on [n8n.cloud](https://n8n.cloud/){:target=_blank .external link} or custom plans still varies depending on your subscription.

[PR #6362](https://github.com/n8n-io/n8n/pull/6362){:target=_blank .external link}

### Directory for installing custom nodes

n8n will no longer load custom nodes from its global `node_modules` directory. Instead, you must install (or link) them to `~/.n8n/custom` (or a directory defined by `N8N_CUSTOM_EXTENSIONS`). Custom nodes that are npm packages will be located in `~/.n8n/nodes`.
If you have custom nodes that were linked using `npm link` into the global `node_modules` directory, you need to link them again, into `~/.n8n/nodes` instead.

[PR #6396](https://github.com/n8n-io/n8n/pull/6396){:target=_blank .external link}

### WebSockets

The `N8N_PUSH_BACKEND` environment variable can be used to configure one of two available methods for pushing updates to the user interface: `sse` and `websocket`. Starting with n8n 1.0, `websocket` is the default method.

[PR #6196](https://github.com/n8n-io/n8n/pull/6196){:target=_blank .external link}

### Date transformation functions

n8n provides various transformation functions that operate on dates. These functions may return either a JavaScript `Date` or a Luxon `DateTime` object. With the new behavior, the return type always matches the input. If you call a date transformation function on a `Date`, it returns a `Date`. Similarly, if you call it on a `DateTime` object, it returns a `DateTime` object.

To identify any workflows and nodes that might be impacted by this change, you can use this [utility workflow](https://n8n.io/workflows/1929-v1-helper-find-params-with-affected-expressions/){:target=_blank .external link}.

For more information about date transformation functions, please refer to the [official documentation](/code/builtin/data-transformation-functions/dates.md).

[PR #6435](https://github.com/n8n-io/n8n/pull/6435){:target=_blank .external link}

### Execution data retention

Starting from n8n 1.0, all successful, failed, and manual workflow executions will be saved by default. These settings can be modified for each workflow under "Workflow Settings," or globally using the respective environment variables. Additionally, the `EXECUTIONS_DATA_PRUNE` setting will be enabled by default, with `EXECUTIONS_DATA_PRUNE_MAX_COUNT` set to 10,000. These default settings are designed to prevent performance degradation when using SQLite. Make sure to configure them according to your individual requirements and system capacity.

[PR #6577](https://github.com/n8n-io/n8n/pull/6577){:target=_blank .external link}

### Removed N8N_USE_DEPRECATED_REQUEST_LIB

The legacy `request` library has been deprecated for some time now. As of n8n 1.0, the ability to fall back to it in the HTTP Request node by setting the `N8N_USE_DEPRECATED_REQUEST_LIB` environment variable has been fully removed. The HTTP Request node will now always use the new `HttpRequest` interface.

If you build custom nodes, refer to [HTTP request helpers](/integrations/creating-nodes/build/reference/http-helpers.md) for more information on migrating to the new interface.

[PR #6413](https://github.com/n8n-io/n8n/pull/6413){:target=_blank .external link}

### Removed WEBHOOK_TUNNEL_URL

As of version 0.227.0, n8n has renamed the `WEBHOOK_TUNNEL_URL` configuration option to `WEBHOOK_URL`. In n8n 1.0, `WEBHOOK_TUNNEL_URL` has been removed. Update your setup to reflect the new name. For more information about this configuration option, refer to [the docs](/hosting/configuration/configuration-examples/webhook-url.md).

[PR #1408](https://github.com/n8n-io/n8n/pull/1408){:target=_blank .external link}

### Remove Node 16 support

n8n now requires Node 18.17.0 or above.

## Updating to n8n 1.0

1. Create a full backup of n8n.
2. n8n recommends updating to the latest n8n 0.x release before updating to n8n 1.x. This will allow you to pinpoint any potential issues to the correct release. Once you have verified that n8n 0.x starts up without any issues, proceed to the next step.
3. Carefully read the [Deprecations](#deprecations) and [Breaking Changes](#breaking-changes) sections above to assess how they may affect your setup.
4. Update to n8n 1.0:
	* During beta (before July 24th 2023): If using Docker, pull the `next` Docker image.
	* After July 24th 2023: If using Docker, pull the `latest` Docker image.
5. If you encounter any issues, redeploy the previous n8n version and restore the backup.

## Reporting issues

If you encounter any issues during the process of updating to n8n 1.0, please seek help in the community [forum](https://community.n8n.io/){:target=_blank .external link}.

## Thank you

We would like to take a moment to express our gratitude to all of our users for their continued support and feedback. Your contributions are invaluable in helping us make n8n the best possible automation tool. We're excited to continue working with you as we move forward with the release of version 1.0 and beyond. Thank you for being a part of our journey!


---

<!-- Source: docs/choose-n8n.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Choose between our Cloud service, or self-hosting options. Learn more about licenses and n8n payment plans.
contentType: overview
---

# Choose your n8n

This section contains information on n8n's range of platforms, pricing plans, and licenses.

## Platforms

There are different ways to set up n8n depending on how you intend to use it:

* [n8n Cloud](/manage-cloud/overview.md): hosted solution, no need to install anything.
* [Self-host](/hosting/index.md): recommended method for production or customized use cases.
	* [npm](/hosting/installation/npm.md)
	* [Docker](/hosting/installation/docker.md)
	* [Server setup guides](/hosting/installation/server-setups/index.md) for popular platforms
* [Embed](/embed/index.md): n8n Embed allows you to white label n8n and build it into your own product. Contact n8n on the [Embed website](https://n8n.io/embed/){:target=_blank .external-link} for pricing and support.

--8<-- "_snippets/self-hosting/warning.md"


## Licenses

n8n's [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md){:target=\_blank .external-link} and [n8n Enterprise License](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md){:target=\_blank .external-link} are based on the [fair-code](https://faircode.io/) model.

For a detailed explanation of the license, refer to [Sustainable Use License](/sustainable-use-license.md).

## Free versions

n8n offers the following free options:

* A free trial of Cloud
* A free self-hosted community edition for self-hosted users

## Paid versions

n8n has two paid versions:

* n8n Cloud: choose from a range of paid plans to suit your usage and feature needs.
* Self-hosted: there are both free and paid versions of self-hosted.

For details of the Cloud plans and contact details for Enterprise Self-hosted, refer to [Pricing](https://n8n.io/pricing/){:target=_blank .external-link} on the n8n website.



---

<!-- Source: docs/external-secrets.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: External secrets
description: Use an external secrets vault with n8n.
contentType: howto
---

# External secrets

/// info | Feature availability
* External secrets are available on Enterprise Self-hosted and Enterprise Cloud plans.
* n8n supports AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, Infisical and HashiCorp Vault. 
* n8n doesn't support [HashiCorp Vault Secrets](https://developer.hashicorp.com/hcp/docs/vault-secrets){:target=_blank .external-link}.
///

You can use an external secrets store to manage [credentials](/glossary.md#credential-n8n) for n8n.

n8n stores all credentials encrypted in its database, and restricts access to them by default. With the external secrets feature, you can store sensitive credential information in an external vault, and have n8n load it in when required. This provides an extra layer of security and allows you to manage credentials used across multiple [n8n environments](/source-control-environments/index.md) in one central place.

## Connect n8n to your secrets store

/// note | Secret names
Your secret names can't contain spaces, hyphens, or other special characters. n8n supports secret names containing alphanumeric characters (`a-z`, `A-Z`, and `0-9`), and underscores. n8n currently only supports plaintext values for secrets, not JSON objects or key-value pairs.
///

1. In n8n, go to **Settings** > **External Secrets**.
1. Select **Set Up** for your store provider.
1. Enter the credentials for your provider:
	* Azure Key Vault: Provide your **vault name**, **tenant ID**, **client ID**, and **client secret**. Refer to the Azure documentation to [register a Microsoft Entra ID app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal){:target=_blank .external-link}. n8n supports only single-line values for secrets.
	* AWS Secrets Manager: provide your **access key ID**, **secret access key**, and **region**. The IAM user must have the `secretsmanager:ListSecrets`, `secretsmanager:BatchGetSecretValue`, and `secretsmanager:GetSecretValue` permissions.

		To give n8n access to all secrets in your AWS Secrets Manager, you can attach the following policy to the IAM user:
		```json
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "AccessAllSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:ListSecrets",
						"secretsmanager:BatchGetSecretValue",
 						"secretsmanager:GetResourcePolicy",
						"secretsmanager:GetSecretValue",
						"secretsmanager:DescribeSecret",
						"secretsmanager:ListSecretVersionIds",
					],
					"Resource": "*"
				}
			]
		}
		```

		You can also be more restrictive and give n8n access to select specific AWS Secret Manager secrets. You still need to allow the `secretsmanager:ListSecrets` and `secretsmanager:BatchGetSecretValue` permissions to access all resources. These permissions allow n8n to retrieve ARN-scoped secrets, but don't provide access to the secret values.

		Next, you need set the scope for the `secretsmanager:GetSecretValue` permission to the specific Amazon Resource Names (ARNs) for the secrets you wish to share with n8n. Ensure you use the correct region and account ID in each resource ARNs. You can find the ARN details in the AWS dashboard for your secrets.
		
		For example, the following IAM policy only allows access to secrets with a name starting with `n8n` in your specified AWS account and region:

		```json
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "ListingSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:ListSecrets",
						"secretsmanager:BatchGetSecretValue"
					],
					"Resource": "*"
				},
				{
					"Sid": "RetrievingSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:GetSecretValue",
						"secretsmanager:DescribeSecret"
					],
					"Resource": [
						"arn:aws:secretsmanager:us-west-2:123456789000:secret:n8n*"
					]
				}
			]
		}
		```

		For more IAM permission policy examples, consult the [AWS documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_iam-policies.html#auth-and-access_examples_batch){:target=_blank .external-link}.

	* HashiCorp Vault: provide the **Vault URL** for your vault instance, and select your **Authentication Method**.  Enter your authentication details. Optionally provide a namespace.
		- Refer to the HashiCorp documentation for your authentication method:
				[Token auth method](https://developer.hashicorp.com/vault/docs/auth/token){:target=_blank .external-link}  
				[AppRole auth method](https://developer.hashicorp.com/vault/docs/auth/approle){:target=_blank .external-link}  
				[Userpass auth method](https://developer.hashicorp.com/vault/docs/auth/userpass){:target=_blank .external-link}  
		- If you use vault namespaces, you can enter the namespace n8n should connect to. Refer to [Vault Enterprise namespaces](https://developer.hashicorp.com/vault/docs/enterprise/namespaces){:target=_blank .external-link} for more information on HashiCorp Vault namespaces.

	* Infisical: provide a **Service Token**. Refer to Infisical's [Service token](https://infisical.com/docs/documentation/platform/token){:target=_blank .external-link} documentation for information on getting your token. If you self-host Infisical, enter the **Site URL**.

	    /// note | Infisical environment
		Make sure you select the correct Infisical environment when creating your token. n8n will load secrets from this environment, and won't have access to secrets in other Infisical environments. n8n only support service tokens that have access to a single environment.
		///

	    /// note | Infisical folders
	 	n8n doesn't support [Infisical folders](https://infisical.com/docs/documentation/platform/folder){:target=_blank .external-link}.
		///

	* Google Cloud Platform: provide a **Service Account Key** (JSON) for a service account that has at least these roles: `Secret Manager Secret Accessor` and `Secret Manager Secret Viewer`. Refer to Google's [service account documentation](https://cloud.google.com/iam/docs/service-account-overview){:target=_blank .external-link} for more information.

1. **Save** your configuration.
1. Enable the provider using the **Disabled / Enabled** toggle.


## Use secrets in n8n credentials

To use a secret from your store in an n8n credential:

1. Create a new credential, or open an existing one.
1. On the field where you want to use a secret:
	1. Hover over the field.
	1. Select **Expression**.
1. In the field where you want to use a secret, enter an [expression](/glossary.md#expression-n8n) referencing the secret name:
	```js
	{{ $secrets.<vault-name>.<secret-name> }}
	```
	`<vault-name>` is either `vault` (for HashiCorp) or `infisical` or `awsSecretsManager`. Replace `<secret-name>` with the name as it appears in your vault.

## Using external secrets with n8n environments

n8n's [Source control and environments](/source-control-environments/index.md) feature allows you to create different n8n environments, backed by Git. The feature doesn't support using different credentials in different instances. You can use an external secrets vault to provide different credentials for different environments by connecting each n8n instance to a different vault or project environment.

For example, you have two n8n instances, one for development and one for production. You use Infisical for your vault. In Infisical, create a project with two environments, development and production. Generate a token for each Infisical environment. Use the token for the development environment to connect your development n8n instance, and the token for your production environment to connect your production n8n instance.

## Using external secrets in projects

To use external secrets in an [RBAC project](/user-management/rbac/index.md), you must have an [instance owner or instance admin](/user-management/account-types.md) as a member of the project.

## Troubleshooting

### Infisical version changes

Infisical version upgrades can introduce problems connecting to n8n. If your Infisical connection stops working, check if there was a recent version change. If so, report the issue to help@n8n.io.

### Only set external secrets on credentials owned by an instance owner or admin

Due to the permissions that instance owners and admins have, it's possible for owners and admins to update credentials owned by another user with a secrets expression. This will appear to work in preview for an instance owner or admin, but the secret won't resolve when the workflow runs in production. 

Only use external secrets for credentials that are owned by an instance admin or owner. This ensures they resolve correctly in production.


---

<!-- Source: docs/glossary.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n Glossary
description: A glossary of terms commonly used when working with n8n and related software.
contentType: reference
---

#### AI agent

AI agents are artificial intelligence systems capable of responding to requests, making decisions, and performing real-world tasks for users. They use large language models (LLMs) to interpret user input and make decisions about how to best process requests using the information and resources they have available.

#### AI chain

AI chains allow you to interact with large language models (LLMs) and other resources in sequences of calls to components. AI chains in n8n don't use persistent memory, so you can't use them to reference previous context (use AI agents for this).

#### AI embedding

Embeddings are numerical representations of data using vectors. They're used by AI to interpret complex data and relationships by mapping values across many dimensions. Vector databases, or vector stores, are databases designed to store and access embeddings.

#### AI groundedness

In AI, and specifically in retrieval-augmented generation (RAG) contexts, groundedness and ungroundedness are measures of how much a model's responses accurately reflect source information. The model uses its source documents to generate grounded responses, while ungrounded responses involve speculation or hallucination unsupported by those same sources.

#### AI reranking

Reranking is a technique that refines the order of a list of candidate documents to improve the relevance of search results. Retrieval-Augmented Generation (RAG) and other applications use reranking to prioritize the most relevant information for generation or downstream tasks.

#### AI memory

In an AI context, memory allows AI tools to persist message context across interactions. This allows you to have a continuing conversations with AI agents, for example, without submitting ongoing context with each message. In n8n, AI agent nodes can use memory, but AI chains can't.

#### AI retrieval-augmented generation (RAG)

Retrieval-augmented generation, or RAG, is a technique for providing LLMs access to new information from external sources to improve AI responses. RAG systems retrieve relevant documents to ground responses in up-to-date, domain-specific, or proprietary knowledge to supplement their original training data. RAG systems often rely on vector stores to manage and search this external data efficiently.

#### AI tool

In an AI context, a tool is an add-on resource that the AI can refer to for specific information or functionality when responding to a request. The AI model can use a tool to interact with external systems or complete specific, focused tasks.

#### AI vector store

Vector stores, or vector databases, are databases designed to store numerical representations of information called embeddings.

#### API

APIs, or application programming interfaces, offer programmatic access to a service's data and functionality. APIs make it easier for software to interact with external systems. They're often offered as an alternative to traditional user-focused interfaces accessed through web browsers or UI.

#### canvas (n8n)

The canvas is the main interface for building workflows in n8n's editor UI. You use the canvas to add and connect nodes to compose workflows.

#### cluster node (n8n)

In n8n, cluster nodes are groups of nodes that work together to provide functionality in a workflow. They consist of a root node and one or more sub nodes that extend the node's functionality.

#### credential (n8n)

In n8n, credentials store authentication information to connect with specific apps and services. After creating credentials with your authentication information (username and password, API key, OAuth secrets, etc.), you can use the associated app node to interact with the service.

#### data pinning (n8n)

Data pinning allows you to temporarily freeze the output data of a node during workflow development. This allows you to develop workflows with predictable data without making repeated requests to external services. Production workflows ignore pinned data and request new data on each execution.

#### editor (n8n)

The n8n editor UI allows you to create and manage workflows. The main area is the canvas, where you can compose workflows by adding, configuring, and connecting nodes. The side and top panels allow you to access other areas of the UI like credentials, templates, variables, executions, and more.

#### entitlement (n8n)

In n8n, entitlements grant n8n instances access to plan-restricted features for a specific period of time.

Floating entitlements are a pool of entitlements that you can distribute among various n8n instances. You can re-assign a floating entitlement to transfer its access to a different n8n instance.

#### evaluation (n8n)

In n8n, evaluation allows you to tag and organize execution history and compare it against new executions. You can use this to understand how your workflow performs over time as you make changes. In particular, this is useful while developing AI-centered workflows.

#### expression (n8n)

In n8n, expressions allow you to populate node parameters dynamically by executing JavaScript code. Instead of providing a static value, you can use the n8n expression syntax to define the value using data from previous nodes, other workflows, or your n8n environment.

#### LangChain

LangChain is an AI-development framework used to work with large language models (LLMs). LangChain provides a standardized system for working with a wide variety of models and other resources and linking different components together to build complex applications.

#### Large language model (LLM)

Large language models, or LLMs, are AI machine learning models designed to excel in natural language processing (NLP) tasks. They're built by training on large amounts of data to develop probabilistic models of language and other data.

#### node (n8n)

In n8n, nodes are individual components that you compose to create workflows. Nodes define when the workflow should run, allow you to fetch, send, and process data, can define flow control logic, and connect with external services.

#### project (n8n)

n8n projects allow you to separate workflows, variables, and credentials into separate groups for easier management. Projects make it easier for teams to collaborate by sharing and compartmentalizing related resources.

#### root node (n8n)

Each n8n cluster node contains a single root nodes that defines the main functionality of the cluster. One or more sub nodes attach to the root node to extend its functionality.

#### sub node (n8n)

n8n cluster nodes consist of one or more sub nodes connected to a root node. Sub nodes extend the functionality of the root node, providing access to specific services or resources or offering specific types of dedicated processing, like calculator functionality, for example.

#### template (n8n)

n8n templates are pre-built workflows designed by n8n and community members that you can import into your n8n instance. When using templates, you may need to fill in credentials and adjust the configuration to suit your needs.

#### trigger node (n8n)

A trigger node is a special node responsible for executing the workflow in response to certain conditions. All production workflows need at least one trigger to determine when the workflow should run.

#### workflow (n8n)

An n8n workflow is a collection of nodes that automate a process. Workflows begin execution when a trigger condition occurs and execute sequentially to achieve complex tasks.

<!-- To do
#### OAuth
#### pagination
#### Role-based access control (RBAC)
#### SAML/SSO
#### two-factor authentication (2FA)
#### webhook
-->


---

<!-- Source: docs/index.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: "Explore n8n Docs: Your Resource for Workflow Automation and Integrations"
description: Access n8n Docs for comprehensive guides on workflow automation and integrations. Learn how to integrate apps and enhance your automation capabilities.
contentType: overview
hide:
  - path
---

# Welcome to n8n Docs


This is the documentation for [n8n](https://n8n.io/){:target=_blank .external-link}, a [fair-code](https://faircode.io){:target=_blank .external-link} licensed workflow automation tool that combines AI capabilities with business process automation.

It covers everything from setup to usage and development. It's a work in progress and all [contributions](/help-community/contributing.md) are welcome.


## Where to start

<div class="grid cards" markdown>

-   __Quickstarts__

    Jump in with n8n's quickstart guides.

    [:octicons-arrow-right-24: Try it out](/try-it-out/index.md)

-   __Choose the right n8n for you__

	Cloud, npm, self-host . . . 

    [:octicons-arrow-right-24: Options](/choose-n8n.md)


-   __Explore integrations__

    Browse n8n's integrations library.

    [:octicons-arrow-right-24: Find your apps](/integrations/index.md)

-   __Build AI functionality__

    n8n supports building AI functionality and tools.

    [:octicons-arrow-right-24: Advanced AI](/advanced-ai/index.md)    
</div>

## About n8n

n8n (pronounced n-eight-n) helps you to connect any app with an API with any other, and manipulate its data with little or no code.

* Customizable: highly flexible workflows and the option to build custom nodes.
* Convenient: use the npm or Docker to try out n8n, or the Cloud hosting option if you want us to handle the infrastructure.
* Privacy-focused: self-host n8n for privacy and security.


---

<!-- Source: docs/insights.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Insights
contentType: explanation
---

# Insights

Insights gives instance owners and admins visibility into how workflows perform over time. This feature consists of three parts:

- [**Insights summary banner**](#insights-summary-banner): Shows key metrics about your instance from the last 7 days at the top of the overview space.
- [**Insights dashboard**](#insights-dashboard): A more detailed visual breakdown with per-workflow metrics and historical comparisons.
- [**Time saved (Workflow ROI)**](#setting-the-time-saved-by-a-workflow): For each workflow, you can set the number of minutes of work that each production execution saves you.

/// info | Feature availability
The insights summary banner displays activity from the last 7 days for all plans. The insights dashboard is only available on Pro (with limited date ranges) and Enterprise plans. 
///

## Insights summary banner

n8n collects several metrics for both the insights summary banner and dashboard. They include:

- Total production executions (not including sub-workflow executions or manual executions)
- Total failed production executions
- Production execution failure rate
- Time saved (when set on at least one or more active workflows)
- Run time average (including wait time from any wait nodes)

## Insights dashboard

Those on the Pro and Enterprise plans can access the **Insights** section from the side navigation. Each metric from the summary banner is also clickable, taking you to the corresponding chart.

The insights dashboard also has a table showing individual insights from each workflow including total production executions, failed production executions, failure rate, time saved, and run time average. 

## Insights time periods

By default, the insights summary banner and dashboard show a rolling 7 day window with a comparison to the previous period to identify increases or decreases for each metric. On the dashboard, paid plans also display data for other date ranges:

- Pro: 7 and 14 days
- Enterprise: 24 hours, 7 days, 14 days, 30 days, 90 days, 6 months, 1 year

## Setting the time saved by a workflow

For each workflow, you can set the number of minutes of work a workflow saves you each time it runs. You can configure this by navigating to the workflow, selecting the three dots menu in the top right and selecting settings. There you can update the **Estimated time saved** value and save. 

This setting helps you calculate how much time automating a process saves over time vs the manual effort to complete the same task or process. Once set, n8n calculates the amount of time the workflow saves you based on the number of production executions and displays it on the summary banner and dashboard.

## Disable or configure insights metrics collection

If you self-host n8n, you can disable or configure insights and metrics collection using [environment variables](/hosting/configuration/environment-variables/insights.md).

## Insights FAQs
<!-- vale from-microsoft.HeadingPunctuation = NO -->

### Which executions do n8n use to calculate the values in the insights banner and dashboard?

n8n insights only collects data from production executions (for example, those from active workflows triggered on a schedule or a webhook) from the main (parent) workflow. This means that it doesn't count manual (test) executions or executions from sub-workflows or error workflows.

### Does n8n use historic execution data when upgrading to a version with insights?

n8n only starts collecting data for insights once you update to the first supported version (1.89.0). This means it only reports on executions from that point forward and you won't see execution data in insights from prior periods.


---

<!-- Source: docs/keyboard-shortcuts.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
tags:
  - Keyboard
  - Move canvas
  - Move nodes
  - Drag and drop
description: Keyboard shortcuts available in n8n.
hide:
  - tags
contentType: reference
---

# Keyboard shortcuts and controls

n8n provides keyboard shortcuts for some actions.

## Workflow controls
 
 - **Ctrl** + **Alt** + **n**: create new workflow
 - **Ctrl** + **o**: open workflow
 - **Ctrl** + **s**: save the current workflow 
 - **Ctrl** + **z**: undo
 - **Ctrl** + **shift** + **z**: redo
 - **Ctrl** + **Enter**: execute workflow

## Canvas

### Move the canvas

 - **Ctrl** + **Left Mouse Button** + drag: move node view
 - **Ctrl** + **Middle mouse button** + drag: move node view
 - **Space** + drag: move node view
 - **Middle mouse button** + drag: move node view
 - Two fingers on a touch screen: move node view

### Canvas zoom

- **+** or **=**: zoom in
- **-** or **_**: zoom out
- **0**: reset zoom level
- **1**: zoom to fit workflow
- **Ctrl** + **Mouse wheel**: zoom in/out

### Nodes on the canvas

- **Double click** on a node: open the node details
- **Ctrl/Cmd** + **Double click** on a sub-workflow node: open the sub-workflow in a new tab
- **Ctrl** + **a**: select all nodes
- **Ctrl** + **v**: paste nodes
- **Shift** + **s**: add sticky note

### With one or more nodes selected in canvas

 - **ArrowDown**: select sibling node below the current one
 - **ArrowLeft**: select node left of the current one
 - **ArrowRight**: select node right of the current one
 - **ArrowUp**: select sibling node above the current one
 - **Ctrl** + **c**: copy
 - **Ctrl** + **x**: cut
 - **D**: deactivate
 - **Delete**: delete
 - **Enter**: open
 - **F2**: rename
 - **P**: pin data in node. Refer to [Data pinning](/data/data-pinning.md) for more information.
 - **Shift** + **ArrowLeft**: select all nodes left of the current one
 - **Shift** + **ArrowRight**: select all nodes right of the current one
 - **Ctrl/Cmd** + **Shift** + **o** on a sub-workflow node: open the sub-workflow in a new tab 

## Node panel

 - **Tab**: open the Node Panel
 - **Enter**: insert selected node into workflow
 - **Escape**: close Node panel

### Node panel categories

- **Enter**: insert node into workflow, collapse/expand category, open subcategory
- **ArrowRight**: expand category, open subcategory 
- **ArrowLeft**: collapse category, close subcategory view

## Within nodes

- **=**: in an empty parameter input, this switches to [expressions](/glossary.md#expression-n8n) mode.


---

<!-- Source: docs/learning-path.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: A suggested learning path to get started with n8n through tutorials, courses, and step-by-step guides.
contentType: overview
---
This guide outlines a series of tutorials and resources designed to get you started with n8n. 

It's not necessary to complete all items listed to start using n8n. Use this as a reference to navigate to the most relevant parts of the documentation and other resources according to your needs.

## Join the community

n8n has an active community where you can get and offer help. Connect, share, and learn with other n8n users:

- [Ask questions](https://community.n8n.io/t/readme-welcome-to-the-n8n-community/44381){:target=_blank .external-link} and [make feature requests](https://community.n8n.io/c/feature-requests){:target=_blank .external-link} in the Community Forum.
- [Report bugs](https://github.com/n8n-io/n8n/issues){:target=_blank .external-link} and [contribute](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md){:target=_blank .external-link} on GitHub.

## Set up your n8n

If you don't have an account yet, sign up to a [free trial on n8n Cloud](https://app.n8n.cloud/register){:target=_blank .external-link} or install n8n's community edition with [Docker](/hosting/installation/docker.md) (recommended) or [npm](/hosting/installation/npm.md). See [Choose your n8n](/choose-n8n.md) for more details.

## Try it out

Start with the quickstart guides to help you get up and running with building basic workflows. 

- [A very quick quickstart](/try-it-out/quickstart.md)
- [A longer introduction](/try-it-out/tutorial-first-workflow.md)
- [Build an AI workflow in n8n](/advanced-ai/intro-tutorial.md)

## Structured Courses

n8n offers two sets of courses.

### Video courses

Learn key concepts and n8n features, while building examples as you go.

- The [Beginner](https://www.youtube.com/playlist?list=PLlET0GsrLUL59YbxstZE71WszP3pVnZfI){:target=_blank .external-link} course covers the basics of n8n.
- The [Advanced](https://www.youtube.com/playlist?list=PLlET0GsrLUL5bxmx5c1H1Ms_OtOPYZIEG){:target=_blank .external-link} course covers more complex workflows, more technical nodes, and enterprise features

### Text courses

Build more complex workflows while learning key concepts along the way. Earn a badge and an avatar in your community profile. 

- [Level 1: Beginner Course](https://blog.n8n.io/announcing-the-n8n-certification-course-for-beginners-level-1/){:target=_blank .external-link}
- [Level 2: Intermediate Course](https://blog.n8n.io/announcing-course-level-two/){:target=_blank .external-link}

## Self-hosting n8n

Explore various [self-hosting options in n8n](/hosting/index.md). If you’re not sure where to start, these are two popular options: 

- [Hosting n8n on DigitalOcean](/hosting/installation/server-setups/digital-ocean.md)
- [Hosting n8n on Amazon Web Services](/hosting/installation/server-setups/aws.md)

## Build a node

If you can't find a node for a specific app or a service, you can build a node yourself and share with the community. See what others have built on [npm website](https://www.npmjs.com/search?q=keywords:n8n-community-node-package){:target=_blank .external-link}. 

- [Build a declarative-style node](/integrations/creating-nodes/build/declarative-style-node.md)
- [Learn how to build your own n8n nodes (Youtube Video)](https://www.youtube.com/live/OI6zHJ56eW0?si=SMD7L1J5fZ2mf79W){:target=_blank .external-link}

## Stay updated
- Follow new features and bug fixes in the [Release Notes](/release-notes.md)
- Follow n8n on socials: [Twitter/X](https://twitter.com/n8n_io){:target=_blank .external-link}, [Discord](https://discord.com/invite/vWwMVThRta){:target=_blank .external-link}, [LinkedIn](https://www.linkedin.com/company/n8n/){:target=_blank .external-link}, [YouTube](https://www.youtube.com/@n8n-io){:target=_blank .external-link}


---

<!-- Source: docs/license-key.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: License key
description: How to activate your license key.
contentType: howto
---

# License Key

To enable certain licensed features, you must first activate your license. You can do this either through the UI or by setting environment variables.

## Add a license key using the UI

In your n8n instance:

1. Log in as **Admin** or **Owner**.
1. Select **Settings** > **Usage and plan**.
1. Select **Enter activation key**.
1. Paste in your license key.
1. Select **Activate**.

## Add a license key using an environment variables

In your n8n configuration, set `N8N_LICENSE_ACTIVATION_KEY` to your license key. If the instance already has an activated license, this variable will have no effect.

Refer to [Environment variables](/hosting/configuration/configuration-methods.md) to learn more about configuring n8n.

## Allowlist the license server IP addresses

n8n uses Cloudflare to host the license server. As the specific IP addresses can change, you need to allowlist the [full range of Cloudflare IP addresses](https://www.cloudflare.com/ips/) to ensure n8n can always reach the license server.


---

<!-- Source: docs/log-streaming.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Stream events from n8n to your logging tools.
contentType: howto
---

# Log streaming

/// info | Feature availability
Log streaming is available on Enterprise Self-hosted and Cloud plans.
///

Log streaming allows you to send events from n8n to your own logging tools. This allows you to manage your n8n monitoring in your own alerting and logging processes.

## Set up log streaming

To use log streaming, you have to add a streaming destination.

1. Navigate to **Settings** > **Log Streaming**.
2. Select **Add new destination**.
3. Choose your destination type. n8n opens the **New Event Destination** modal.
4. In the **New Event Destination** modal, enter the configuration information for your event destination. These depend on the type of destination you're using.
5. Select **Events** to choose which events to stream.
6. Select **Save**.

/// note | Self-hosted users
If you self-host n8n, you can configure additional log streaming behavior using [Environment variables](/hosting/configuration/environment-variables/logs.md#log-streaming).
///
## Events

The following events are available. You can choose which events to stream in **Settings** > **Log Streaming** > **Events**.

* Workflow
	* Started
	* Success
	* Failed
* Node executions
	* Started
	* Finished
* Audit
	* User signed up
	* User updated
	* User deleted
	* User invited
	* User invitation accepted
	* User re-invited
	* User email failed
	* User reset requested
	* User reset
	* User credentials created
	* User credentials shared
	* User credentials updated
	* User credentials deleted
	* User API created
	* User API deleted
	* Package installed
	* Package updated
	* Package deleted
	* Workflow created
	* Workflow deleted
	* Workflow updated
* AI node logs
	* Memory get messages
	* Memory added message
	* Output parser get instructions
	* Output parser parsed
	* Retriever get relevant documents
	* Embeddings embedded document
	* Embeddings embedded query
	* Document processed
	* Text splitter split
	* Tool called
	* Vector store searched
	* LLM generated
	* Vector store populated
* Runner
	* Task requested
	* Response received
* Queue
	* Job enqueued
	* Job dequeued
	* Job completed
	* Job failed
	* Job stalled

## Destinations

n8n supports three destination types:

* A syslog server
* A generic webhook
* A Sentry client


---

<!-- Source: docs/release-notes.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Release notes
description: Release notes detailing new features and bug fixes for n8n.
tags:
  - release
  - release notes
  - changelog
hide:
  - tags
contentType: reference
---
<!-- vale off -->
# Release notes

New features and bug fixes for n8n.

You can also view the [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} in the GitHub repository.

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

--8<-- "_snippets/update-n8n.md"

## Semantic versioning in n8n

n8n uses [semantic versioning](https://semver.org/){:target=_blank .external-link}. All version numbers are in the format `MAJOR.MINOR.PATCH`. Version numbers increment as follows:

* MAJOR version when making incompatible changes which can require user action.
* MINOR version when adding functionality in a backward-compatible manner.
* PATCH version when making backward-compatible bug fixes.

/// note | Older versions
You can find the release notes for older versions of n8n [here](/release-notes/0-x.md)
///



## n8n@1.102.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.101.0...n8n@1.102.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-07-07

/// note | Next version
This is the `next` version. n8n recommends using the `latest` version. The `next` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12){:target=_blank .external-link}.
///

This release contains core updates, editor improvements, new nodes, node updates, and bug fixes.

### Contributors

[marty-sullivan](https://github.com/marty-sullivan){:target=_blank .external-link}  
[cesars-gh](https://github.com/cesars-gh){:target=_blank .external-link}  
[dudanogueira](https://github.com/dudanogueira){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.101.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.101.0...n8n@1.101.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-07-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.101.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.100.0...n8n@1.101.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-30



This release contains core updates, editor improvements, node updates, and bug fixes.

### Contributors

[luka-mimi](https://github.com/luka-mimi){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.100.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.100.0...n8n@1.100.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-25

/// note | Latest version
This is the `latest` version. n8n recommends using the `latest` version. The `next` version may be unstable. To report issues, use the [forum](https://community.n8n.io/c/questions/12){:target=_blank .external-link}.
///





This release contains a bug fix.


For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.100.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.99.0...n8n@1.100.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-23



This release contains core updates, editor improvements, a new node, node updates, and bug fixes.

### Support for OIDC (OpenID Connect) authentication

You can now use OIDC (OpenID Connect) as an authentication method for Single Sign-On (SSO).

This gives enterprise teams more flexibility to integrate n8n with their existing identity providers using a widely adopted and easy-to-manage standard. OIDC is now available alongside SAML, giving Enterprises the choice to select what best fits their internal needs.

### Project admins can now commit to Git within environments

Project admins now have the ability to commit workflow and credential changes directly to Git through the environments feature. This update streamlines the workflow deployment process by giving project-level admins direct control over committing their changes. It also ensures that the those who know their workflows best can review and commit updates themselves, without needing to involve instance-level admins.

[Learn more about source control environments](/source-control-environments/index.md)


### Contributors

[aliou](https://github.com/aliou){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.99.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.99.0...n8n@1.99.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-19







This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.98.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.98.1...n8n@1.98.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-18



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.99.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.98.0...n8n@1.99.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-16

This release contains performance improvements, core updates, editor changes, node updates, and bug fixes.

### Automatically name nodes

Default node names now update automatically based on the resource and operation selected, so you’ll always know what a node does at a glance.

This adds clarity to your canvas and saves time renaming nodes manually.

Don’t worry, automatic naming won’t break references. And, and if you’ve renamed a node yourself, we’ll leave it just the way you wrote it.

<br>
<video src="/_video/release-notes/automatic_node_naming.mp4" controls width="100%"></video>
<br>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.98.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.98.0...n8n@1.98.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-12



This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.98.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.97.0...n8n@1.98.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-11



This release contains performance improvements, core updates, editor changes, node updates, a new node, and bug fixes.

### Contributors

[luka-mimi](https://github.com/luka-mimi){:target=_blank .external-link}  
[Alexandero89](https://github.com/Alexandero89){:target=_blank .external-link}  
[khoazero123](https://github.com/khoazero123){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.97.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.97.0...n8n@1.97.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-04







This release contains backports.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.95.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.2...n8n@1.95.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-03



This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.97.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.96.0...n8n@1.97.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-02

This release contains new features, performance improvements and bug fixes.

### Convert to sub-workflow

Large, monolithic workflows can slow things down. They’re harder to maintain, tougher to debug, and more difficult to scale. With sub-workflows, you can take a more modular approach, breaking up big workflows into smaller, manageable parts that are easier to reuse, test, understand, and explain.

Until now, creating sub-workflows required copying and pasting nodes manually, setting up a new workflow from scratch, and reconnecting everything by hand. **Convert to sub-workflow** allows you to simplify this process into a single action, so you can spend more time building and less time restructuring.

<br>
<video src="/_video/release-notes/convert_to_sub-workflow.mp4" controls width="100%"></video>
<br>

**How it works**

1. Highlight the nodes you want to convert to a sub-workflow. These must:
    - Be fully connected, meaning no missing steps in between them
    - Start from a single starting node
    - End with a single node
2. Right-click to open the context menu and select **Convert to sub-workflow**
    - Or use the shortcut: `Alt + X`
3. n8n will:
    - Open a new tab containing the selected nodes
    - Preserve all node parameters as-is
    - Replace the selected nodes in the original workflow with a **Call My Sub-workflow** node

*Note*: You will need to manually adjust the field types in the Start and Return nodes in the new sub-workflow.

This makes it easier to keep workflows modular, performant, and easier to maintain.

Learn more about [sub-workflows](/flow-logic/subworkflows.md).

This release contains performance improvements and bug fixes.


### Contributors

[maatthc](https://github.com/maatthc){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.96.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.0...n8n@1.96.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-06-02

/// warning | Build failure
This release failed to build. Please use `1.97.0` instead.
///

This release contains API updates, core changes, editor improvements, node updates, and bug fixes.

### API support for assigning users to projects

You can now use the API to add and update users within projects. This includes:

- Assigning existing or pending users to a project with a specific role
- Updating a user’s role within a project
- Removing users from one or more projects

This update now allows you to use the API to add users to both the instance and specific projects, removing the need to manually assign them in the UI. 

### Add pending users to project member assignment

You can now add **pending users,** those who have been invited but haven't completed sign-up, to projects as members.

This change lets you configure a user's project access upfront, without waiting for them to finish setting up their account. It eliminates the back-and-forth of managing access post-sign-up, ensuring users have the right project roles immediately upon joining.

### Contributors

[matthabermehl](https://github.com/matthabermehl){:target=_blank .external-link}  
[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.95.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.1...n8n@1.95.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-29

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.95.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.95.0...n8n@1.95.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.94.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.94.0...n8n@1.94.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.95.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.94.0...n8n@1.95.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-26

This release contains core updates, editor improvements, node updates, and bug fixes.

<div class="n8n-new-features" markdown> 

### Evaluations for AI workflows

We’ve added a feature to help you iterate, test, and compare changes to your AI automations before pushing them to production so you can achieve more predictability and make better decisions.<br><br>

When you're building with AI, a small prompt tweak or model swap might improve results with some inputs, while quietly degrading performance with others. But without a way to evaluate performance across many inputs, you’re left guessing whether your AI is actually getting better when you make a change.  <br><br>

By implementing **Evaluations for AI workflows** in n8n, you can assess how your AI performs across a range of inputs by adding a dedicated path in your workflow for running test cases and applying custom metrics to track results. This helps you build viable proof-of-concepts quickly, iterate more effectively, catch regressions early, and make more confident decisions when your AI is in production.<br><br>


<iframe width="560" height="315" src="https://www.youtube.com/embed/5LlF196PKaE?si=TcwM0JyhjsRKDb3x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<br><br>

#### Evaluation node and tab

The **Evaluation node** includes several operations that, when used together, enable end-to-end AI evaluation.

<br> 
<figure markdown="span">
    ![Evaluation node](/_images/release-notes/Evaluations_node.png)
    <figcaption>Evaluation node</figcaption>
</figure>
<br>

Use this node to:

- Run your AI logic against a wide range of test cases in the same execution
- Capture the outputs of those test cases
- Score the results using your own metrics or LLM-as-judge logic
- Isolate a testing path to only include the nodes and logic you want to evaluate <br>

The **Evaluations tab** enables you to review test results in the n8n UI, perfect for comparing runs, spotting regressions, and viewing performance over time.
<br><br>

#### 🛠 How evaluations work

The evaluation path runs alongside your normal execution logic and only activates when you want—making it ideal for testing and iteration. <br><br>

Get started by selecting an AI workflow you want to evaluate that includes one or more LLM or Agent nodes. <br>

1. Add an **Evaluation** node with the **On new Evaluation event** operation. This node will act as an additional trigger you’ll run only when testing. Configure it to read your dataset from Google Sheets, with each row representing a test input.<br>

    > 💡  Better datasets mean better evaluations. Craft your dataset from a variety of test cases, including edge cases and typical inputs, to get meaningful feedback on how your AI performs. Learn more and access sample datasets [here](/advanced-ai/evaluations/light-evaluations.md/#1-create-a-dataset).

2. Add a second **Evaluation** node using the **Set Outputs** operation after the part of the workflow you're testing—typically after an LLM or Agent node. This captures the response and writes it back to your dataset in Google Sheets.
3. To evaluate output quality, add a third **Evaluation** node with the **Set Metrics** operation at a point after you’ve generated the outputs. You can develop workflow logic, custom calculations, or add an LLM-as-Judge to score the outputs. Map these metrics to your dataset in the node’s parameters. <br>

    > 💡 Well-defined metrics = smarter decisions. Scoring your outputs based on similarity, correctness, or categorization can help you track whether changes are actually improving performance. Learn more and get links to example templates [here](/advanced-ai/evaluations/metric-based-evaluations.md/#2-calculate-metrics). 
    
<br>

<figure markdown="span">
    ![Evaluation workflow](/_images/release-notes/Evaluations_workflow.png)
    <figcaption>Evaluation workflow</figcaption>
</figure>
<br>

When the Evaluation trigger node is executed, it runs each input in our dataset through your AI logic. This continues until all test cases are processed, a limit is reached, or you manually stop the execution. Once your evaluation path is set up, you can update your prompt, model, or workflow logic—and re-run the Evaluation trigger node to compare results. If you’ve added metrics, they’ll appear in the Evaluations tab. <br><br>

In some instances, you may want to isolate your testing path to make iteration faster or to avoid executing downstream logic.  In this case, you can add an Evaluation node with the `Check If Evaluating` operation to ensure only the expected nodes run when performing evaluations. <br><br>

#### Things to keep in mind

Evaluations for AI Workflows are designed to fit  into your development flow, with more enhancements on the way. For now, here are a few things to note:

- Test datasets are currently managed through Google Sheets. You’ll need a Google Sheets credential to run evaluations.
- Each workflow supports one evaluation at a time. If you’d like to test multiple segments, consider splitting them into sub-workflows for more flexibility.
- Community Edition supports one single evaluation. Pro and Enterprise plans allow unlimited evaluations.
- AI Evaluations are not enabled for instances in scaling mode at this time. <br>

You can find details, tips, and common troubleshooting info [here](https://docs.n8n.io/advanced-ai/evaluations/tips-and-common-issues/). <br><br>

 👉 Learn more about the AI evaluation strategies and practical implementation techniques during a **livestream on July 2nd, 2025 at 5:00 p.m GMT+2**. [Sign up](https://lu.ma/rfniiq2c). 

</div> 

### Contributors

[Phiph](https://github.com/Phiph){:target=_blank .external-link}  
[cesars-gh](https://github.com/cesars-gh){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.94.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.93.0...n8n@1.94.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-19

This release contains editor improvements, an API update, node updates, new nodes, and bug fixes.

<div class="n8n-new-features" markdown> 

### Verified community nodes on Cloud

We’ve expanded the n8n ecosystem and unlocked a new level of flexibility for all users including those on n8n Cloud! Now you can access a select set of community nodes and partner integrations without leaving the canvas. This means you install and automate with a wider range of integrations without leaving your workspace. The power of the community is now built-in.

This update focuses on three major improvements:

- **Cloud availability**: Community nodes are no longer just for self-hosted users. A select set of nodes is now available on n8n Cloud.
- **Built-in discovery**: You can find and explore these nodes right from the Nodes panel without leaving the editor or searching on npm.
- **Trust and verification**: Nodes that appear in the editor have been manually vetted for quality and security. These verified nodes are marked with a checkmark.

We’re starting with a selection of around 25 nodes, including some of the most-used community-built packages and partner-supported integrations. For this phase, we focused on nodes that don’t include external package dependencies - helping streamline the review process and ensure a smooth rollout.
<br>
<br>

This is just the start. We plan to expand the library gradually, bringing even more verified nodes into the editor along with the powerful and creative use cases they unlock. In time, our criteria will evolve, opening the door to a wider range of contributions while keeping quality and security in focus.
<br>
<br>

Learn more about this update and find out which nodes are already installable from the editor in our [blog](https://blog.n8n.io/community-nodes-available-on-n8n-cloud/) post. 

<br>

 💻 **Use a verified node**

Make sure you're on **n8n version 1.94.0** or later and the instance Owner has enabled verified community nodes. On Cloud, this can be done from the Admin Panel. For self-hosted instances, please refer to [documentation](/hosting/configuration/environment-variables/nodes.md). In both cases, verified nodes are enabled by default.

- Open the **Nodes panel** from the editor
- Search for the Node. Verified nodes are indicated by a shield 🛡️
- Select the node and click **Install**

<br>
<video src="/_video/release-notes/Community-nodes-node-panel.mp4" controls width="100%"></video>
<br>

Once an Owner installs a node, everyone on the instance can start using it—just drag, drop, and connect like any other node in your workflow.

<br>

🛠️ **Build a node and get it verified**

Want your node to be verified and discoverable from the editor? Here’s how to get involved:

1. Review the [community node verification guidelines](/integrations/creating-nodes/build/reference/verification-guidelines.md).
2. If you’re building something new, follow the recommendations for [creating nodes](/integrations/creating-nodes/overview.md).
3. Check your design against the [UX guidelines](/integrations/creating-nodes/build/reference/ux-guidelines.md).
4. [Submit your node](/integrations/creating-nodes/deploy/submit-community-nodes.md) to npm.
5. Request verification by filling out [this form](https://internal.users.n8n.cloud/form/f0ff9304-f34a-420e-99da-6103a2f8ac5b).

<br>

**Already built a node? Raise your hand!**

If you’ve already published a community node and want it considered for verification, make sure it meets the requirements noted above, then let us know by submitting the interest [form](https://internal.users.n8n.cloud/form/f0ff9304-f34a-420e-99da-6103a2f8ac5b). We’re actively curating the next batch and would love to include your work.

</div> 


### Extended logs view

When workflows get complex, debugging can get... clicky. That’s where an extended **Logs View** comes in. Now you can get a clearer path to trace executions, troubleshoot issues, and understand the behavior of a complete workflow — without bouncing between node detail views. 

This update brings a unified, always-accessible panel to the bottom of the canvas, showing you each step of the execution as it happens. Whether you're working with loops, sub-workflows, or AI agents, you’ll see a structured view of everything that ran, in the order it ran—with input, output, and status info right where you need it.

You can jump into node details when you want to dig deeper, or follow a single item through every step it touched. Real-time highlighting shows you which nodes are currently running or have failed, and you’ll see total execution time for any workflow—plus token usage for AI workflows to help monitor performance. And if you're debugging across multiple screens? Just pop the logs out and drag them wherever you’d like.

⚙️**What it does**

- Adds a **Logs view** to the bottom of the canvas that can be opened or collapsed. (Chat also appears here if your workflow uses it).
- Displays a **hierarchical list of nodes** in the order they were executed—including expanded views of sub-workflows.
- Allows you to **click a node in hierarchy** to preview inputs and outputs directly, or jump into the full Node Details view with a link.
- Provides ability to **toggle** input and output data on and off.
- Highlights each node **live as it runs**, showing when it starts, completes, or fails.
- Includes **execution history** view to explore past execution data in a similar way.
- Shows **roll-up stats** like total execution time and total AI tokens used (for AI-enabled workflows).
- Includes a  **“pop out”** button to open the logs as a floating window—perfect for dragging to another screen while debugging.

🛠️**How to**

To access the expanded logs view, click on the Logs bar at the bottom of the canvas. The view is also opens up when you open the chat window on the bottom of the page.

### Contributors

[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  
[feelgood-interface](https://github.com/feelgood-interface){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.93.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.0...n8n@1.93.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-12

This release contains core updates, editor improvements, new nodes, node updates, and bug fixes.

### Faster ways to open sub-workflows

We’ve added several new ways to navigate your multi-workflow automations faster.

From any workflow with a sub-workflow node:

🖱️ Right-click on a sub-workflow node and select `Open sub-workflow` from the context menu

⌨️ Keyboard shortcuts

- **Windows:** `CTRL + SHIFT + O` or `CTRL + Double Click`
- **Mac:** `CMD + SHIFT + O` or `CMD + Double Click`

These options will bring your sub-workflow up in a new tab.

### Archive workflows

If you’ve ever accidentally removed a workflow, you’ll appreciate the new archiving feature. Instead of permanently deleting workflows with the Remove action, workflows are now archived by default. This allows you to recover them if needed.

**How to:**

- **Archive a workflow** - Select **Archive** from the Editor UI menu. It has replaced the **Remove** action.
- **Find archived workflows** - Archived workflows are hidden by default. To find your archived workflows, select the option for **Show archived workflows** in the workflow filter menu.
- **Permanently delete a workflow** - Once a workflow is archived, you can **Delete** it from the  options menu.
- **Recover a workflow** - Select **Unarchive** from the options menu.

**Keep in mind:** 

- Workflows archival requires the same permissions as required previously for removal.
- You cannot select archived workflows as sub-workflows to execute
- Active workflows are deactivated when they are archived
- Archived workflows can not be edited

### Contributors

[LeaDevelop](https://github.com/LeaDevelop){:target=_blank .external-link}  
[ayhandoslu](https://github.com/ayhandoslu){:target=_blank .external-link}  
[valentina98](https://github.com/valentina98){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.92.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.1...n8n@1.92.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.91.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.2...n8n@1.91.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.92.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.92.0...n8n@1.92.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.92.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.0...n8n@1.92.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-05

This release contains core updates, editor improvements, node updates, and bug fixes.

### Partial Execution for AI Tools

We’ve made it easier to build and iterate on AI agents in n8n. You can now run and test specific tools without having to execute the entire agent workflow.

Partial execution is especially useful when refining or troubleshooting parts of your agent logic. It allows you to test changes incrementally, without triggering full agent runs, reducing unnecessary AI calls, token usage, and downstream activity. This makes iteration faster, more cost-efficient, and more precise when working with complex or multi-step AI workflows.

Partial execution for AI tools is available now for all tools - making it even easier to build, test, and fine-tune AI agents in n8n.

<br>
<video src="/_video/release-notes/AI-agent-partial-execution.mp4" controls width="100%"></video>
<br>

**How to:**

To use this feature you can either:

- Click the **Play** button on the tool you want to execute directly from the canvas view.
- Open the tool’s **Node Details View** and select **"Test step"** to run it from there.

If you have previously run the workflow, the input and output will be prefilled with data from the last execution. A pop-up form will open where you can manually fill in the parameters before executing your test.

### Extended logs view

When workflows get complex, debugging can get... clicky. That’s where an extended **Logs View** comes in. Now you can get a clearer path to trace executions, troubleshoot issues, and understand the behavior of a complete workflow — without bouncing between node detail views. 

This update brings a unified, always-accessible panel to the bottom of the canvas, showing you each step of the execution as it happens. Whether you're working with loops, sub-workflows, or AI agents, you’ll see a structured view of everything that ran, in the order it ran—with input, output, and status info right where you need it.

You can jump into node details when you want to dig deeper, or follow a single item through every step it touched. Real-time highlighting shows you which nodes are currently running or have failed, and you’ll see total execution time for any workflow—plus token usage for AI workflows to help monitor performance. And if you're debugging across multiple screens? Just pop the logs out and drag them wherever you’d like.

⚙️**What it does**

- Adds a **Logs view** to the bottom of the canvas that can be opened or collapsed. (Chat also appears here if your workflow uses it).
- Displays a **hierarchical list of nodes** in the order they were executed—including expanded views of sub-workflows.
- Allows you to **click a node in hierarchy** to preview inputs and outputs directly, or jump into the full Node Details view with a link.
- Provides ability to **toggle** input and output data on and off.
- Highlights each node **live as it runs**, showing when it starts, completes, or fails.
- Includes **execution history** view to explore past execution data in a similar way.
- Shows **roll-up stats** like total execution time and total AI tokens used (for AI-enabled workflows).
- Includes a  **“pop out”** button to open the logs as a floating window—perfect for dragging to another screen while debugging.

🛠️**How to**

To access the expanded logs view, click on the Logs bar at the bottom of the canvas. The view is also opens up when you open the chat window on the bottom of the page.

### Insights enhancements for Enterprise

Two weeks after the launch of [Insights](/insights.md), we’re releasing some enhancements designed for enterprise users.

- **Expanded time ranges**. You can now filter insights over a variety of time periods, from the last 24 hours up to 1 year. Pro users are limited to 7 day and 14 day views.  
- **Hourly granularity**. Drill down into the last 24 hours of production executions with hourly granularity, making it easier to analyze workflows and quickly identify issues.  

These updates provide deeper visibility into workflow history, helping you uncover trends over longer periods and detect problems sooner with more precise reporting.

<br> 
<figure markdown="span">
    ![Filter insights](/_images/release-notes/Insights-drill-down.png)
    <figcaption>Filter insights</figcaption>
</figure>
<br>

### Contributors

[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.91.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.1...n8n@1.91.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-05

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.90.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.2...n8n@1.90.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-05

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.91.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.91.0...n8n@1.91.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-05-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.91.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.0...n8n@1.91.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-28

This release contains core updates, editor improvements, node updates, and bug fixes.

### Breadcrumb view from the canvas

We’ve added **breadcrumb navigation directly on the canvas**, so you can quickly navigate to any of a workflow’s parent folders right from the canvas.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.90.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.1...n8n@1.90.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-25

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.90.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.90.0...n8n@1.90.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-22

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.90.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.0...n8n@1.90.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-22

This release contains core updates, editor updates, node updates, performance improvements, and bug fixes.

### Extended HTTP Request tool functionality
We’ve brought the full power of the HTTP Request node to the HTTP Request tool in AI workflows. That means your AI Agents now have access to all the advanced configuration options—like Pagination, Batching, Timeout, Redirects, Proxy support, and even cURL import.

<br>
<video src="/_video/release-notes/http-request-tool.mp4" controls width="100%"></video>
<br>

This update also includes support for the `$fromAI` function to dynamically generate the right parameters based on the context of your prompt — making API calls smarter, faster, and more flexible than ever.

**How to:**

- Open your AI Agent node in the canvas.
- Click the **‘+’ icon** to add a new tool connection.
- In the **Tools panel**, select HTTP **Request Tool.**
- Configure it just like you would a regular **HTTP Request node** — including advanced options

👉 Learn more about configuring the [HTTP Request tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md).


### Scoped API keys
Users on the Enterprise plan can now create API keys with specific scopes to control exactly what each key can access.

<figure markdown="span">
    ![Scoped API keys](/_images/release-notes/scoped-API-keys.png)
    <figcaption>Scoped API keys</figcaption>
</figure>

Previously, API keys had full read/write access across all endpoints. While sometimes necessary, this level of access can be excessive and too powerful for most use cases.  Scoped API keys allow you to limit access to only the resources and actions a service or user actually needs.

**What’s new**

When creating a new API key, you can now:

- Select whether the key has read, write, or both types of access.  
- Specify which resources the key can interact with.  

Supported scopes include:

- Variables — list, create, delete  
- Security audit — generate reports  
- Projects — list, create, update, delete  
- Executions — list, read, delete  
- Credentials — list, create, update, delete, move  
- Workflows — list, create, update, delete, move, add/remove tags  

Scoped API keys give you more control and security. You can limit access to only what’s needed, making it safer to work with third parties and easier to manage internal API usage.

### Drag and Drop in Folders

Folders just got friendlier. With this release, you can now **drag and drop workflows and folders** — making it even easier to keep things tidy.

Need to reorganize? Just select a workflow or folder and drag it into another folder or breadcrumb location. It’s a small change that makes a big difference when managing a growing collection of workflows.

<br>
<video src="/_video/release-notes/Drag-and-drop-folders.mp4" controls width="100%"></video>
<br>

📁 Folders are available to all [registered](/hosting/community-edition-features.md#registered-community-edition) users—jump in and get your workspace in order!

### Contributors

[Zordrak](https://github.com/Zordrak){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.89.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.1...n8n@1.89.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-16

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.89.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.89.0...n8n@1.89.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.89.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.88.0...n8n@1.89.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-14

This release contains API updates, core updates, editor updates, a new node, node updates, and bug fixes.

<div class="n8n-new-features" markdown> 

### Insights 

We're rolling out [Insights](/insights.md), a new dashboard to monitor how your workflows are performing over time. It's designed to give admins (and owners) better visibility of their most important workflow metrics and help troubleshoot potential issues and improvements. <br> 
<br>

In this first release, we’re introducing a summary banner, the insights dashboard, and time saved per execution. <br> <br>

#### 1. Summary banner
A new banner on the overview page that gives instance admins and owners a birds eye view of key metrics over the last 7 days.

<figure markdown="span">
    ![Summary banner](/_images/release-notes/Insights-summary-banner.png)
    <figcaption>Insights summary banner</figcaption>
</figure>

Available metrics:

- Total production executions
- Total failed executions
- Failure rate
- Average runtime of all workflows
- Estimated time saved

This overview is designed to help you stay on top of workflow activity at a glance. It is available for all plans and editions. <br> <br>

#### 2. Insights dashboard
On Pro and Enterprise plans, a new dashboard offers a deeper view into workflow performance and activity. 

<figure markdown="span">
    ![Insights dashboard](/_images/release-notes/Insights-dashboard.png)
    <figcaption>Insights dashboard</figcaption>
</figure>

The dashboard includes:

- Total production executions over time, including a comparison of successful and failed executions
- Per-workflow breakdowns of key metrics
- Comparisons with previous periods to help spot changes in usage or behavior
- Runtime average and failure rate over time

#### 3. Time saved per execution
Within workflow settings, you can now assign a “time saved per execution” value to any workflow. This makes it possible to track the impact of your workflows and make it easier to share this visually with other teams and stakeholders.<br><br>

This is just the beginning for Insights: the next phase will introduce more advanced filtering and comparisons, custom date ranges, and additional monitoring capabilities. 

</div>

### Node updates
- We added a credential check for the Salesforce node
- We added SearXNG as a tool for AI agents

You can now search within subfolders, making it easier to find workflows across all folder levels. Just type in the search bar and go. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.88.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.0...n8n@1.88.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-10

This release contains new features, new nodes, performance improvements, and bug fixes.

<div class="n8n-new-features" markdown> 


### Model Context Protocol (MCP) nodes
MCP aims to standardise how LLMs like Claude, ChatGPT, or Cursor can interact with tools or integrate data for their agents. Many providers - both established or new - are adopting MCP as a standard way to build agentic systems. It is an easy way to either expose your own app as a server, making capabilities available to a model as tools, or as a client that can call on tools outside of your own system. <br>

While it’s still early in the development process, we want to give you access to our new MCP nodes. This will help us understand your requirements better and will also let us converge on a great general solution quicker. <br>

We are adding two new nodes: 

- a MCP [Server Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md) for any workflow  
- a MCP [Client Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) for the AI Agent  

The MCP Server Trigger turns n8n into an MCP server, providing n8n tools to models running outside of n8n. You can run multiple MCP servers from your n8n instance. The MCP Client Tool connects LLMs - and other intelligent agents - to any MCP-enabled service through a single interface. <br>

Max from our DevRel team created an official walkthrough for you to get started: 

<br>

[![Studio](/_images/release-notes/MCP-YouTube-thumb.jpg)](https://youtu.be/45WPU7P-1QQ?feature=shared)
<figure markdown="span">
    <figcaption>[Studio Update #04](https://youtu.be/45WPU7P-1QQ?feature=shared)</figcaption>
</figure>


### MCP Server Trigger
The MCP Server Trigger turns n8n into an MCP server, providing n8n tools to models running outside of n8n. The node acts as an entry point into n8n for MCP clients. It operates by exposing a URL that MCP clients can interact with to access n8n tools. This means your n8n workflows and integrations are now available to models run elsewhere. Pretty neat. 

<figure markdown="span">
    ![MCP Server Trigger](/_images/release-notes/MCP-Server-Trigger.png)
    <figcaption>MCP Server Trigger</figcaption>
</figure>

[Explore the MCP Server Trigger docs](/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md)

### MCP Client Tool
The MCP Client Tool node is a MCP client, allowing you to use the tools exposed by an external MCP server. You can connect the MCP Client Tool node to your models to call external tools with n8n agents. In this regard it is similar to using a n8n tool with your AI agent. One advantage is that the MCP Client Tool can access multiple tools on the MCP server at once, keeping your canvas cleaner and easier to understand. 

<figure markdown="span">
    ![MCP Client Tool](/_images/release-notes/MCP-Client-Tool.png)
    <figcaption>MCP Client Tools</figcaption>
</figure>

[Explore the MCP Client Tool docs](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md)

</div>

### Node updates

- Added a node for Azure Cosmos DB  
- Added a node for Milvus Vector Store  
- Updated the Email Trigger (IMAP) node  

### Contributors

[adina-hub](https://github.com/adina-hub){:target=_blank .external-link}  
[umanamente](https://github.com/umanamente){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.87.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.1...n8n@1.87.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-09

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.86.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.86.0...n8n@1.86.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-09

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.87.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.87.0...n8n@1.87.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-08

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.87.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.86.0...n8n@1.87.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-04-07

This release contains new nodes, node updates, API updates, core updates, editor updates, and bug fixes.

### Contributors

[cesars-gh](https://github.com/cesars-gh){:target=_blank .external-link}  
[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  
[Pash10g](https://github.com/Pash10g){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.86.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.0...n8n@1.86.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-31

This release contains API updates, core updates, editor improvements, node updates, and bug fixes.

### Contributors

[Aijeyomah](https://github.com/Aijeyomah){:target=_blank .external-link}  
[ownerer](https://github.com/ownerer){:target=_blank .external-link}  
[ulevitsky](https://github.com/ulevitsky){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.85.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.3...n8n@1.85.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.84.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.2...n8n@1.84.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.84.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.1...n8n@1.84.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.85.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.2...n8n@1.85.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.85.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.1...n8n@1.85.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-25

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.85.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.85.0...n8n@1.85.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.85.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.0...n8n@1.85.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-24

This release contains a new node, a new credential, core updates, editor updates, node updates, and bug fixes.

### Folders
What can we say about folders? Well, they’re super handy for categorizing just about everything and they’re finally available for your n8n workflows. Tidy up your workspace with unlimited folders and nested folders. Search for workflows within folders. It’s one of the ways we’re making it easier to organize your n8n instances more effectively.  

**How to use it:** 

Create and manage folders within your personal space or within projects. You can also create workflows from within a folder. You may need to restart your instance in order to activate folders.

<figure markdown="span">
    ![Folders](/_images/release-notes/Folders.png
)
    <figcaption>It's a folder alright</figcaption>
</figure>
<br>

Folders are available for all [registered](/hosting/community-edition-features.md#registered-community-edition) users so get started with decluttering your workspace now and look for more features (like drag and drop) to organize your instances soon.

### Enhancements to Form Trigger Node

Recent updates to the Form Trigger node have made it a more powerful tool for building business solutions. These enhancements provide more flexibility and customization, enabling teams to create visually engaging and highly functional workflows with forms.

- **HTML customization:** Add custom HTML to forms, including embedded images and videos, for richer user experiences.  
- **Custom CSS support**: Apply custom styles to user-facing components to align forms with your brand’s look and feel. Adjust fonts, colors, and spacing for a seamless visual identity.
- **Form previews:** Your form’s description and title will pull into previews of your form when sharing on social media or messaging apps, providing a more polished look.  
- **Hidden fields:** Use query parameters to add hidden fields, allowing you to pass data—such as a referral source—without exposing it to the user.  
- **New responses options:** Respond to user submissions in multiple ways including text, HTML, or a downloadable file (binary format). This enables forms to display rich webpages or deliver digital assets such as dynamically generated invoices or personalized certificates.  

<figure markdown="span">
    ![Form with custom CSS applied](/_images/release-notes/Forms_with_custom_CSS_and_HTML.png)
    <figcaption>Form with custom CSS applied</figcaption>
</figure>
<br>

These improvements elevate the Form Trigger node beyond a simple workflow trigger, transforming it into a powerful tool for addressing use cases from data collection and order processing to custom content creation.

### Contributors

[Fank](https://github.com/Fank){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.84.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.84.0...n8n@1.84.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-18

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.84.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.0...n8n@1.84.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-17

This release contains a new node, node updates, editor updates, and bug fixes.

### Contributors

[Pash10g](https://github.com/Pash10g){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.83.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.1...n8n@1.83.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-14

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.82.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.3...n8n@1.82.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-14

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.82.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.2...n8n@1.82.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-13

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.83.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.83.0...n8n@1.83.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.83.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.0...n8n@1.83.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-12

This release contains bug fixes and an editor update.

### Schema Preview

Schema Preview lets you view and work with a node’s expected output without executing it or adding credentials, keeping you in flow while building.

- **See expected node outputs instantly.** View schemas for over 100+ nodes to help you design workflows efficiently without extra steps.  
- **Define workflow logic first, take care of credentials later.** Build your end-to-end workflow without getting sidetracked by credential setup.  
- **Avoid unwanted executions when building.** Prevent unnecessary API calls, unwanted data changes, or potential third-party service costs by viewing outputs without executing nodes.  

**How to use it:**

- Add a node with Schema Preview support to your workflow.
- Open the next node in the sequence - Schema Preview data appears in the Node Editor where you would typically find it in the Schema View.
- Use Schema Preview fields just like other schema data - drag and drop them into parameters and settings as needed.

<br>
<video src="/_video/release-notes/Schema_preview.mp4" controls width="100%"></video>
<br>

Don’t forget to add the required credentials before putting your workflow into production.

### Contributors

[pemontto](https://github.com/pemontto){:target=_blank .external-link}  
[Haru922](https://github.com/Haru922){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.82.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.1...n8n@1.82.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.82.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.82.0...n8n@1.82.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.82.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.0...n8n@1.82.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-03

This release contains core updates, editor updates, new nodes, node updates, new credentials, credential updates, and bug fixes.

### Tidy up
Tidy up instantly aligns nodes, centers stickies, untangles connections, and brings structure to your workflows. Whether you're preparing to share a workflow or just want to improve readability, this feature saves you time and makes your logic easier to follow. Clean, well-organized workflows aren't just nicer to look at—they’re also quicker to understand.

**How to:** 

Open the workflow you want to tidy, then choose one of these options:

- Click the **Tidy up** button in the bottom-left corner of the canvas (it looks like a broom 🧹)
- Press **Shift + Alt + T** on your keyboard
- Right-click anywhere on the canvas and select **Tidy up workflow**

Want to tidy up just part of your workflow? Select the specific nodes you want to clean up first - Tidy up will only adjust those, along with any stickies behind them.

<br>
<video src="/_video/release-notes/tidy_up.mp4" controls width="100%"></video>
<br>


### Multiple API keys
n8n now supports multiple API keys, allowing users to generate and manage separate keys for different workflows or integrations. This improves security by enabling easier key rotation and isolation of credentials. Future updates will introduce more granular controls. <br>

<figure markdown="span">
    ![Multiple API keys](/_images/release-notes/Multiple-API-keys.png)
    <figcaption>Multiple API keys</figcaption>
</figure>
<br>

### Contributors

[Rostammahabadi](https://github.com/Rostammahabadi){:target=_blank .external-link}  
[Lanhild](https://github.com/Lanhild){:target=_blank .external-link}  
[matthiez](https://github.com/matthiez){:target=_blank .external-link}  
[feelgood-interface](https://github.com/feelgood-interface){:target=_blank .external-link}  
[adina-hub](https://github.com/adina-hub){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.81.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.3...n8n@1.81.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-03

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.81.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.2...n8n@1.81.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-03-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.81.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.1...n8n@1.81.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-28

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.5

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.4...n8n@1.80.5){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-28

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.3...n8n@1.80.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-27

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.81.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.81.0...n8n@1.81.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.81.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.0...n8n@1.81.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-24

This release contains bug fixes, a core update, editor improvements, and a node update.

### Improved partial executions
The new execution engine for partial executions ensures that testing parts of a workflow in the builder closely mirrors production behaviour. This makes iterating with updated run-data faster and more reliable, particularly for complex workflows.

Before, user would test parts of a workflow in the builder that didn't consistently reflect production behaviour, leading to unexpected results during development.

This update aligns workflow execution in the builder with production behavior.

Here is an example for loops:

Before
<br>

<video src="/_video/release-notes/Partial-execution-loop-before.mp4" controls width="100%"></video>
<br>
After
<br>

<video src="/_video/release-notes/Partial-execution-loop-after.mp4" controls width="100%"></video>


For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.2...n8n@1.80.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.79.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.3...n8n@1.79.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.1...n8n@1.80.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.79.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.2...n8n@1.79.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.80.0...n8n@1.80.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.79.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.1...n8n@1.79.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.80.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.0...n8n@1.80.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-17

This release contains bug fixes and an editor improvement.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.75.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.2...n8n@1.75.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.74.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.3...n8n@1.74.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.79.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.79.0...n8n@1.79.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.78.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.78.0...n8n@1.78.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.77.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.3...n8n@1.77.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.76.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.3...n8n@1.76.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.79.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.78.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-12

This release contains new features, node updates, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.77.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.2...n8n@1.77.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.78.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.78.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-05

This release contains new features, node updates, and bug fixes.

### Contributors

[mocanew](https://github.com/mocanew){:target=_blank .external-link}  
[Timtendo12](https://github.com/Timtendo12){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.77.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.1...n8n@1.77.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.76.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.2...n8n@1.76.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.77.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.77.0...n8n@1.77.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.76.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.1...n8n@1.76.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-02-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.77.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.0...n8n@1.77.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-29

This release contains new features, editor updates, new nodes, new credentials, node updates, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.76.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.76.0...n8n@1.76.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-23

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.76.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.0...n8n@1.76.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-22

This release contains new features, editor updates, new credentials, node improvements, and bug fixes.

### Contributors

[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  
[GKdeVries](https://github.com/GKdeVries){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.75.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.1...n8n@1.75.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.74.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.2...n8n@1.74.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.75.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.75.0...n8n@1.75.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.74.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.1...n8n@1.74.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.75.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.0...n8n@1.75.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-15

This release contains bug fixes and editor updates.

### Improved consistency across environments
We added new UX and automatic changes improvements resulting in a better consistency between your staging and production instances.

Previously, users faced issues like:  

- Lack of visibility into required credential updates when pulling changes  
- Incomplete synchronization, where changes — such as deletions — weren’t always applied across environments  
- Confusing commit process, making it unclear what was being pushed or pulled  

We addressed these by:

- Clearly indicating required credential updates when pulling changes  
- Ensuring deletions and other modifications sync correctly across environments  
- Improving commit selection to provide better visibility into what’s being pushed  
<br>
<figure markdown="span">
    ![Commit modal](/_images/release-notes/Commit-modal.png)
    <figcaption>Commit modal</figcaption>
</figure>
<br>
<figure markdown="span">
    ![Pull notification](/_images/release-notes/Pull-notification.png)
    <figcaption>Pull notification</figcaption>
</figure>
<br>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.74.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.74.0...n8n@1.74.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-09

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.74.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.73.0...n8n@1.74.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2025-01-08

This release contains new features, a new node, node updates, performance improvements and bug fixes.

<div class="n8n-new-features" markdown>

### Overhauled Code node editing experience
We added a ton of new helpers to the Code node, making edits of your code much faster and more comfortable. You get:

- TypeScript autocomplete  
- TypeScript linting  
- TypeScript hover tips  
- Search and replace  
- New keyboard shortcuts based on the VSCode keymap  
- Auto-formatting using prettier (Alt+Shift+F)  
- Remember folded regions and history after refresh  
- Multi cursor  
- Type function in the Code node using JSDoc types  
- Drag and drop for all Code node modes  
- Indentation markers  

We build this on a web worker architecture so you won't have to suffer from performance degradation while typing. <br>
<br>
To get the full picture, check out our Studio update with Max and Elias, where they discuss and demo the new editing experience. 👇 <br>

[![Studio](/_images/release-notes/The_Studio_thumbnail_Code_node.jpg)](https://youtu.be/De1E58MPaMQ?t=645)
<figure markdown="span">
    <figcaption>[Studio Update #04](https://youtu.be/De1E58MPaMQ?t=645)</figcaption>
</figure>

</div>

### New node: Microsoft Entra ID
Microsoft Entra ID (formerly known as Microsoft Azure Active Directory or Azure AD) is used for cloud-based identity and access management. [The new node](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md) supports a wide range of Microsoft Entra ID features, which includes creating, getting, updating, and deleting users and groups, as well as adding users to and removing them from groups. 

### Node updates

- [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): Vector stores can now be directly used as tools for the agent
- [Code](/code/builtin/overview.md): Tons of new speed and convenience features, see above for details  
- [Google Vertex Chat](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md): Added option to specify the GCP region for the Google API credentials  
- [HighLevel](/integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md): Added support for calendar items  


We also added a custom [projects](/user-management/rbac/projects.md) icon selector on top of the available emojis. Pretty!

### Contributors

[igatanasov](https://github.com/igatanasov){:target=_blank .external-link}  
[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  
[feelgood-interface](https://github.com/feelgood-interface){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.73.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.73.0...n8n@1.73.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-19

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.73.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.72.0...n8n@1.73.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-19

This release contains node updates, performance improvements, and bug fixes.

### Node updates

- [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): Updated descriptions for Chat Trigger options
- [Facebook Graph API](/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md): Updated for API v21.0
- [Gmail](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md): Added two new options for the `Send and wait` operation, free text and custom form  
- [Linear Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md): Added support for admin scope  
- [MailerLite](/integrations/builtin/app-nodes/n8n-nodes-base.mailerlite.md): Now supports the new API  
- [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md):  Added two new options for the `Send and wait` operation, free text and custom form  

We also added credential support for [SolarWinds IPAM](/integrations/builtin/credentials/solarwindsipam.md) and [SolarWinds Observability](/integrations/builtin/credentials/solarwindsobservability.md). 

Last, but not least, we [improved the schema view performance in the node details view by 90%](https://github.com/n8n-io/n8n/pull/12180) and added drag and drop re-ordering to parameters. This comes in very handy in the [If](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) or [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) nodes. 

### Contributors

[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[mickaelandrieu](https://github.com/mickaelandrieu){:target=_blank .external-link}  
[Stamsy](https://github.com/Stamsy){:target=_blank .external-link}  
[pbdco](https://github.com/pbdco){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.72.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.72.0...n8n@1.72.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-12





This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.71.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.2...n8n@1.71.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-12



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.72.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.0...n8n@1.72.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-11

This release contains node updates, usability improvements, and bug fixes.

### Node updates

- [AI Transform](/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md): The `maximum context length` error now retries with reduced payload size
- [Redis](/integrations/builtin/app-nodes/n8n-nodes-base.redis.md): Added support for `continue on fail`

### Improved commit modal 

We added filters and text search to the commit modal when working with [Environments](/source-control-environments/index.md). This will make committing easier as we provide more information and better visibility. Environments are available on the Enterprise plan. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.71.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.1...n8n@1.71.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-10





This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.70.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.3...n8n@1.70.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-10



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.71.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.71.0...n8n@1.71.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-06

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.70.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.2...n8n@1.70.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-05

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.71.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.2...n8n@1.71.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-04

This release contains node updates, performance improvements, and bug fixes.

<div class="n8n-new-features" markdown>

### Task runners for the Code node in public beta
We're introducing a significant performance upgrade to the Code node with our new Task runner system. This enhancement moves JavaScript code execution to a separate process, improving your workflow execution speed while adding better isolation.

<figure markdown="span">
    ![Task runners overview](/_images/hosting/configuration/task-runner-concept.png)
    <figcaption>Task runners overview</figcaption>
</figure>

Our benchmarks show up to 6x improvement in workflow executions using Code nodes - from approximately 6 to 35 executions per second. All these improvements happen under the hood, keeping your Code node experience exactly the same.

The Task runner comes in two modes:

- Internal mode (default): Perfect for getting started, automatically managing task runners as child processes  
- External mode: For advanced hosting scenarios requiring maximum isolation and security

Currently, this feature is opt-in and can be enabled using [environment variables](/hosting/configuration/environment-variables/task-runners.md). Once stable, it will become the default execution method for Code nodes.

To start using Task runners today, [check out the docs](/hosting/configuration/task-runners.md).

</div>

### Node updates

- [AI Transform node](/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md): We improved the prompt for code generation to transform data
- [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md): We added a warning if `pairedItem` is absent or could not be auto mapped  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.70.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.1...n8n@1.70.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-12-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.70.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.70.0...n8n@1.70.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-29

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.70.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.0...n8n@1.70.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-27

This release contains node updates, performance improvements and bug fixes.

### New canvas in beta
The new canvas is now the default setting for all users. It should bring significant performance improvements and adds a handy minimap. As it is still a beta version you can still revert to the previous version with the three dot menu.  

We're looking forward to your feedback. Should you encounter a bug, you will find a handy button to create an issue at the bottom of the new canvas as well. 

### Node updates
- We added credential support for [Zabbix](/integrations/builtin/credentials/zabbix.md) to the HTTP request node  
- We added new OAuth2 credentials for [Microsoft SharePoint](/integrations/builtin/credentials/microsoft.md)
- The [Slack node](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md#operations) now uses markdown for the approval message when using the `Send and Wait for Approval` operation

### Contributors

[feelgood-interface](https://github.com/feelgood-interface){:target=_blank .external-link}  
[adina-hub](https://github.com/adina-hub){:target=_blank .external-link}  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.68.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.68.0...n8n@1.68.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.69.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.1...n8n@1.69.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-26




This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.69.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.69.0...n8n@1.69.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-25



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.69.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.68.0...n8n@1.69.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-20



This release contains a new feature, node improvements and bug fixes.

### Sub-workflow debugging
We made it much easier to debug sub-workflows by improving their accessibility from the parent workflow. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.68.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.67.1...n8n@1.68.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-13


This release contains node updates, performance improvements and many bug fixes.

<div class="n8n-new-features" markdown>

#### New AI agent canvas chat

We revamped the chat experience for AI agents on the canvas. A neatly organized view instead of a modal hiding the nodes. You can now see the canvas, chat and logs at the same time when testing your workflow. 
<br /><br />

<video src="/_video/release-notes/AI-chat-on-canvas.mp4" controls width="100%"></video>
<br /><br />

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.67.1
View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.67.0...n8n@1.67.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-07

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.67.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.66.0...n8n@1.67.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-11-06

This release contains node updates and bug fixes.

### Node updates

- [AI Transform](/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md): Improved usability  
- [Anthropic Chat Model Node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md): Added Haiku 3.5 support  
- [Convert to File](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md): Added delimiter option for writing to CSV  
- [Gmail Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/index.md): Added option to filter for draft messages  
- [Intercom](/integrations/builtin/app-nodes/n8n-nodes-base.intercom.md): Credential can now be used in the HTTP Request node  
- [Rapid7 InsightVM](/integrations/builtin/credentials/rapid7insightvm.md): Added credential support  

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.66.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.2...n8n@1.66.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-31

This release contains performance improvements, a node update and bug fixes.

### Node update

- [Anthropic Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md): Added support for claude-3-5-sonnet-20241022  

We made updates to how projects and workflow ownership are displayed making them easier to understand and navigate. 

We further improved the performance logic of partial executions, leading to a smoother and more enjoyable building experience. 

### New n8n canvas alpha
We have enabled the alpha version of our new canvas. The canvas is the ‘drawing board’ of the n8n editor, and we’re working on a full rewrite. Your feedback and testing will help us improve it. 
[Read all about it on our community forum](https://community.n8n.io/t/help-us-test-the-new-n8n-canvas-alpha/60070). 


For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.65.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.1...n8n@1.65.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-28

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.64.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.2...n8n@1.64.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.65.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.65.0...n8n@1.65.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.65.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.1...n8n@1.65.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-24

/// warning | [Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md){:target=_blank .external-link}
What changed?
Queue polling via the environment variable `QUEUE_RECOVERY_INTERVAL` has been removed.

When is action necessary?
If you have set `QUEUE_RECOVERY_INTERVAL`, you can remove it as it no longer has any effect.
///

This release contains a new features, new nodes, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

### New node: n8n Form
Use the [n8n Form node](/integrations/builtin/core-nodes/n8n-nodes-base.form.md) to create user-facing forms with multiple pages. You can add other nodes with custom logic between to process user input. Start the workflow with a [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md). 

<figure markdown="span">
    ![A multi-page form with branching](/_images/integrations/builtin/core-nodes/n8n-nodes-base.form/example_image.png)
    <figcaption>A multi-page form with branching</figcaption>
</figure>

Additionally you can: 

- Set default selections with query parameters  
- Define the form with a JSON array of objects
- Show a completion screen and redirect to another URL

</div>

### Node updates
New nodes: 

- [Google Business Profile](/integrations/builtin/app-nodes/n8n-nodes-base.googlebusinessprofile.md) and [Google Business Profile Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md): Use these to integrate Google Business Profile reviews and posts with your workflows  

Enhanced nodes:

- [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): Removed the requirement to add at least one tool  
- [GitHub](/integrations/builtin/app-nodes/n8n-nodes-base.github.md): Added workflows as a resource operation  
- [Structured Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/index.md): Added more user-friendly error messages

For additional security, we improved how we handle multi-factor authentication, hardened config file permissions and introduced JWT for the public API. 

For better performance, we improved how partial executions are handled in loops. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

- [Idan Fishman](https://github.com/idanfishman){:target=_blank .external-link}  

## n8n@1.64.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.1...n8n@1.64.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-24

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.64.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.64.0...n8n@1.64.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-21

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.64.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.4...n8n@1.64.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-16

This release contains a new node, node enhancements, performance improvements and bug fixes.

<div class="n8n-new-features" markdown>

### Enhanced node: Remove Duplicates
The [Remove Duplicates node](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md) got a major makeover with the addition of two new operations: 

- Remove Items Processed in Previous Executions: Compare items in the current input to items from previous executions and remove duplicates  
- Clear Deduplication History: Wipe the memory of items from previous executions.

This makes it easier to only process new items from any data source. For example, you can now more easily poll a Google sheet for new entries by `id` or remove duplicate orders from the same customer by comparing their `order date`. The great thing is, you can now do this within **and across** workflow runs. 

</div>

### New node: Gong
  
The new node for [Gong](/integrations/builtin/app-nodes/n8n-nodes-base.gong.md) allows you to get users and calls to process them further in n8n. Very useful for sales related workflows. 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

- [Sören Uhrbach](https://github.com/soerenuhrbach){:target=_blank .external-link}  

## n8n@1.63.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.3...n8n@1.63.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.62.6

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.5...n8n@1.62.6){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.63.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.2...n8n@1.63.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-15

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.63.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.1...n8n@1.63.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.62.5

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.4...n8n@1.62.5){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.63.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.63.0...n8n@1.63.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.62.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.3...n8n@1.62.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-11

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.63.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.3...n8n@1.63.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-09

/// warning | [Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md){:target=_blank .external-link}
What changed?

- The worker server used to bind to IPv6 by default. It now binds to IPv4 by default.  
- The worker server's `/healthz` used to report healthy status based on database and Redis checks. It now reports healthy status regardless of database and Redis status, and the database and Redis checks are part of `/healthz/readiness`.  

When is action necessary?

- If you experience a port conflict error when starting a worker server using its default port, set a different port for the worker server with `QUEUE_HEALTH_CHECK_PORT`.  
- If you are relying on database and Redis checks for worker health status, switch to checking `/healthz/readiness` instead of `/healthz`.  
///

This release contains new features, node enhancements and bug fixes.

### Node updates

- [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md): Added the option to choose between the default memory connector to provide memory to the assistant or to specify a thread ID    
- [Gmail](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) and [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md): Added custom approval operations to have a human in the loop of a workflow  

We have also optimized the [worker health checks](/hosting/logging-monitoring/monitoring.md) (see breaking change above). 

Each credential now has a seperate url you can link to. This makes sharing much easier. 


For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Pemontto](https://github.com/pemontto){:target=_blank .external-link}  

## n8n@1.62.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.2...n8n@1.62.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-08

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.62.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.62.1...n8n@1.62.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-07

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.62.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.61.0...n8n@1.62.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-10-02

This release contains new features, node enhancements and bug fixes.

/// note | Skipped 1.62.0
We skipped 1.62.0 and went straight to 1.62.1 with an additional fix. 
///

<div class="n8n-new-features" markdown>

#### Additional nodes as tools

We have made additional nodes usable with the [Tools AI Agent node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md). 
<br /><br />

<video src="/_video/release-notes/nodes-as-tools.mp4" controls width="100%"></video>
<br /><br />
Additionally, we have added a `$fromAI()` placeholder function to use with tools, allowing you to dynamically pass information from the models to the connected tools. This function works similarly to placeholders used elsewhere in n8n. 
<br /><br />
Both of these new features enable you to build even more powerful AI agents by drawing directly from the apps your business uses. This makes integrating LLMs into your business processes even easier than before. 

</div>

### Node updates

- [Google BigQuery](/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md): Added option to return numeric values as integers and not strings 
- [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md): Added credential support for Sysdig 
- [Invoice Ninja](/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md): Additional query params for getAll requests 
- [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md): Added the option to use a custom prompt 


Drag and drop insertion on cursor position from schema view is now also enabled for code, SQL and Html fields in nodes. 

Customers with an enterprise license can now rate, tag and highlight execution data in the executions view. To use highlighting, add an [Execution Data Node](/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) (or Code node) to the workflow to set [custom executions data](/workflows/executions/custom-executions-data.md). 

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Benjamin Roedell](https://github.com/benrobot){:target=_blank .external-link}  
[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[manuelbcd](https://github.com/manuelbcd){:target=_blank .external-link}  
[Miguel Prytoluk](https://github.com/mprytoluk){:target=_blank .external-link}  

## n8n@1.61.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.60.1...n8n@1.61.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-25

This release contains new features, node enhancements and bug fixes.

### Node updates

- [Brandfetch](/integrations/builtin/app-nodes/n8n-nodes-base.brandfetch.md): Updated to use the new API
- [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md): Made adding or removing the workflow link to a message easier

Big datasets now render faster thanks to virtual scrolling and execution annotations are harder to delete.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.59.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.3...n8n@1.59.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.60.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.60.0...n8n@1.60.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-20

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.60.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.3...n8n@1.60.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-18

This release contains new features, node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### Queue metrics for workers

You can now [expose and consume metrics from your workers](https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus/). The worker instances have the same metrics available as the main instance(s) and can be configured with [environment variables](/hosting/configuration/environment-variables/endpoints.md).

</div>

You can now customize the maximum file size when uploading files within forms to webhooks. The [environment variable to set](/hosting/configuration/environment-variables/endpoints.md) for this is `N8N_FORMDATA_FILE_SIZE_MAX`. The default setting is 200MiB.

### Node updates
Enhanced nodes:

- [Invoice Ninja](/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md): Added actions for bank transactions
- [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md): Added O1 models to the model select

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}

## n8n@1.59.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.2...n8n@1.59.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-18

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.59.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.1...n8n@1.59.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-17

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.59.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.59.0...n8n@1.59.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.58.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.1...n8n@1.58.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.59.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.1...n8n@1.59.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-11

/// warning | Chat Trigger
If you are using the Chat Trigger in "Embedded Chat" mode, with authentication turned on, you could see errors connecting to n8n if the authentication on the sending/embedded side is mis-configured.
///

This release contains bug fixes and feature enhancements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[oscarpedrero](https://github.com/oscarpedrero){:target=_blank .external-link}

## n8n@1.58.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.58.0...n8n@1.58.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-06

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.58.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.57.0...n8n@1.58.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-09-05

This release contains new features, bug fixes and feature enhancements.

<div class="n8n-new-features" markdown>

#### New node: PGVector Vector Store

This release adds the PGVector Vector Store node. Use this node to interact with the PGVector tables in your PostgreSQL database. You can insert, get, and retrieve documents from a vector table to provide them to a retriever connected to a chain.

</div>

<div class="n8n-new-features" markdown>

#### See active collaborators on workflows

We added collaborator avatars back to the workflow canvas. You will see other users who are active on the workflow, preventing you from overriding each other's work.

<figure markdown="span">
    ![Collaboration avatars](/_images/release-notes/Collaboration-avatar.png)
    <figcaption>Collaboration avatars</figcaption>
</figure>

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.57.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.2...n8n@1.57.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-28

This release contains new features and bug fixes.

<div class="n8n-new-features" markdown>

#### Improved execution queue handling

We are [exposing new execution queue metrics](/hosting/configuration/configuration-examples/prometheus.md) to give users more visibility of the queue length. This helps to inform decisions on horizontal scaling, based on queue status. We have also made querying executions faster.

</div>

<div class="n8n-new-features" markdown>

#### New credentials for the HTTP Request node

We added credential support for Datadog, Dynatrace, Elastic Security, Filescan, Iris, and Malcore to the HTTP Request node making it easier to use existing credentials.

</div>


We also made it easier to select workflows as tools when working with AI agents by implementing a new `workflow selector` parameter type.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Bram Kn](https://github.com/bramkn){:target=_blank .external-link}

## n8n@1.56.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.1...n8n@1.56.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-26

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.56.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.56.0...n8n@1.56.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.56.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.3...n8n@1.56.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-21

This release contains node updates, security and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


### Contributors

[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[Oz Weiss](https://github.com/thewizarodofoz){:target=_blank .external-link}

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.55.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.2...n8n@1.55.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.55.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.1...n8n@1.55.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.55.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.55.0...n8n@1.55.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.54.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.3...n8n@1.54.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.54.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.2...n8n@1.54.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.54.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.1...n8n@1.54.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-14

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.55.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.1...n8n@1.55.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-14

/// warning | [Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md){:target=_blank .external-link}
The N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES environment variable now also blocks access to n8n's static cache directory at ~/.cache/n8n/public.

If you are writing to or reading from a file at n8n's static cache directory via a node, e.g. Read/Write Files from Disk, please update your node to use a different path.
///

This release contains a new feature, a new node, a node update and bug fixes.

<div class="n8n-new-features" markdown>

#### Override the npm registry

This release adds the option to override the npm registry for installing community packages. This is a paid feature.

We now also prevent npm downloading community packages from a compromised npm registry by explicitly using --registry in all npm install commands.

</div>

<div class="n8n-new-features" markdown>

#### New node: AI Transform

This release adds the [AI Transform node](/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md). Use the AI Transform node to generate code snippets based on your prompt. The AI is context-aware, understanding the workflow’s nodes and their data types. The node is only available on [Cloud plans](/manage-cloud/overview.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Okta

This release adds the [Okta node](/integrations/builtin/app-nodes/n8n-nodes-base.okta.md). Use the Okta node to automate work in Okta and integrate Okta with other applications. n8n has built-in support for a wide range of Okta features, which includes creating, updating, and deleting users.

</div>

### Node updates
Enhanced node:

- [MySQL](/integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md)


This release also adds the new schema view for the expression editor modal.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.54.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.54.0...n8n@1.54.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-13

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.53.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.1...n8n@1.53.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-08

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.54.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.1...n8n@1.54.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-07

This release contains new features, node enhancements, bug fixes and updates to our API.

### API update
Our [public REST API](/api/index.md) now supports additional operations:

- Create, delete, and edit roles for users
- Create, read, update and delete projects

Find the details in the [API reference](/api/api-reference.md).

### Contributors

[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[Javier Ferrer González](https://github.com/JavierCane){:target=_blank .external-link}  
[Mickaël Andrieu](https://github.com/mickaelandrieu){:target=_blank .external-link}  
[Oz Weiss](https://github.com/thewizarodofoz){:target=_blank .external-link}  
[Pemontto](https://github.com/pemontto){:target=_blank .external-link}

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.45.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.1...n8n@1.45.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-06

This release contains a bug fix.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.53.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.53.0...n8n@1.53.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-08-02

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.53.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.2...n8n@1.53.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-31

This release contains new features, new nodes, node enhancements, bug fixes and updates to our API.

<div class="n8n-new-features" markdown>

#### Added Google Cloud Platform Secrets Manager support

This release adds [Google Cloud Platform Secrets Manager](/external-secrets.md) to the list of external secret stores. We already support AWS secrets, Azure Key Vault, Infisical and HashiCorp Vault. External secret stores are available under an enterprise license.

</div>

<div class="n8n-new-features" markdown>

#### New node: Information Extractor

This release adds the [Information Extractor node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md). The node is specifically tailored for information extraction tasks. It uses Structured Output Parser under the hood, but provides a simpler way to extract information from text in a structured JSON form.

</div>

<div class="n8n-new-features" markdown>

#### New node: Sentiment Analysis

This release adds the [Sentiment Analysis node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md). The node leverages LLMs to analyze and categorize the sentiment of input text. Users can easily integrate this node into their workflows to perform sentiment analysis on text data. The node is flexible enough to handle various use cases, from basic positive/negative classification to more nuanced sentiment categories.

</div>

### Node updates
Enhanced nodes:

- [Calendly Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md)
- [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md)
- [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md)
- [Shopify](/integrations/builtin/app-nodes/n8n-nodes-base.shopify.md)

### API update
Our [public REST API](/api/index.md) now supports additional operations:

- Create, read, and delete for variables
- Filtering workflows by project
- Transferring workflows

Find the details in the [API reference](/api/api-reference.md).

### Contributors

[feelgood-interface](https://github.com/feelgood-interface){:target=_blank .external-link}  
[Oz Weiss](https://github.com/thewizarodofoz){:target=_blank .external-link}

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.52.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.1...n8n@1.52.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-31

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.52.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.52.0...n8n@1.52.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.51.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.1...n8n@1.51.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.52.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.1...n8n@1.52.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-25


/// warning | [Breaking change](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md){:target=_blank .external-link}
Prometheus metrics enabled via N8N_METRICS_INCLUDE_DEFAULT_METRICS and N8N_METRICS_INCLUDE_API_ENDPOINTS were fixed to include the default n8n_ prefix.

If you are using Prometheus metrics from these categories and are using a non-empty prefix, please update those metrics to match their new prefixed names.
///


This release contains new features, node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### Added Azure Key Vault support

This release adds [Azure Key Vault](/external-secrets.md) to the list of external secret stores. We already support AWS secrets, Infisical and HashiCorp Vault and are working on Google Secrets Manager. External secret stores are available under an enterprise license.

</div>

### Node updates
Enhanced nodes:

- [Pinecone Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)
- [Supabase Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md)
- [Send Email](/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md)

Deprecated nodes:

- OpenAI Model: You can use the OpenAI Chat Model instead
- Google Palm Chat Model: You can use Google Vertex or Gemini instead
- Google Palm Model: You can use Google Vertex or Gemini instead


## n8n@1.51.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.51.0...n8n@1.51.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.50.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.1...n8n@1.50.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.51.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.1...n8n@1.51.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-18

This release contains new nodes, node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: Text Classifier

This release adds the [Text Classifier node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Postgres Chat Memory

This release adds the [Postgres Chat Memory node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Google Vertex Chat Model

This release adds the [Google Vertex Chat Model node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Node updates
- Enhanced nodes: Asana

## n8n@1.50.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.50.0...n8n@1.50.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-16

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.50.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.49.0...n8n@1.50.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-10

This release contains node enhancements and bug fixes.

### Node updates
- Enhanced nodes: Chat Trigger, Google Cloud Firestore, Qdrant Vector Store, Splunk, Telegram
- Deprecated node: Orbit (product shut down)

### Beta Feature Removal
The Ask AI beta feature for the HTTP Request node has been removed from this version

### Contributors
[Stanley Yoshinori Takamatsu](https://github.com/stanleytakamatsu){:target=_blank .external-link}  
[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[jeanpaul](https://github.com/jeanpaul){:target=_blank .external-link}  
[adrian-martinez-onestic](https://github.com/adrian-martinez-onestic){:target=_blank .external-link}  
[Malki Davis](https://github.com/mxdavis){:target=_blank .external-link}


## n8n@1.49.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.3...n8n@1.49.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-03



This release contains a new node, node enhancements, and bug fixes.

### Node updates
- New node added: [Vector Store Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) for the AI Agent
- Enhanced nodes: Zep Cloud Memory, Copper, Embeddings Cohere, GitHub, Merge, Zammad

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors
[Jochem](https://github.com/jvdweerthof){:target=_blank .external-link}  
[KhDu](https://github.com/KhDu){:target=_blank .external-link}  
[Nico Weichbrodt](https://github.com/envy){:target=_blank .external-link}  
[Pavlo Paliychuk](https://github.com/paul-paliychuk){:target=_blank .external-link}


## n8n@1.48.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.2...n8n@1.48.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-03



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.47.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.2...n8n@1.47.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-03

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.48.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.1...n8n@1.48.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.47.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.1...n8n@1.47.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-07-01

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.48.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.48.0...n8n@1.48.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-27

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.48.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.1...n8n@1.48.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-27



This release contains bug fixes and feature enhancements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[KubeAl](https://github.com/KubeAl){:target=_blank .external-link}


## n8n@1.47.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.47.0...n8n@1.47.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-26

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.47.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.46.0...n8n@1.47.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-20

/// warning | Breaking change
Calling `$(...).last()` (or `(...).first()` or `$(...).all()`) without arguments now returns the last item (or first or all items) of the output that connects two nodes. Previously, it returned the item/items of the first output of that node. Refer to the [breaking changes log](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1470){:target=_blank .external-link} for details.
///

This release contains bug fixes, feature enhancements, a new node, node enhancements and performance improvements.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

<div class="n8n-new-features" markdown>

#### New node: HTTP request tool

This release adds the HTTP request tool. You can use it with an AI agent as a tool to collect information from a website or API. Refer to the [HTTP request tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md) for details.

</div>

### Contributors

[Daniel](https://github.com/daniel-alba17){:target=_blank .external-link}  
[ekadin-mtc](https://github.com/ekadin-mtc){:target=_blank .external-link}  
[Eric Francis](https://github.com/EricFrancis12){:target=_blank .external-link}  
[Josh Sorenson](https://github.com/joshsorenson){:target=_blank .external-link}  
Mohammad Alsmadi 
[Nikolai T. Jensen](https://github.com/ch0wm3in){:target=_blank .external-link}  
[n8n-ninja](https://github.com/n8n-ninja){:target=_blank .external-link}  
[pebosi](https://github.com/pebosi){:target=_blank .external-link}  
[Taylor Hoffmann](https://github.com/TaylorHo){:target=_blank .external-link}

## n8n@1.45.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.0...n8n@1.45.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-12


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.46.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.45.0...n8n@1.46.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-12




This release contains feature enhancements, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Jean Khawand](https://github.com/jeankhawand){:target=_blank .external-link}  
[pemontto](https://github.com/pemontto){:target=_blank .external-link}  
[Valentin Coppin](https://github.com/valimero){:target=_blank .external-link}

## n8n@1.44.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.1...n8n@1.44.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-12



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.42.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.1...n8n@1.42.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-10

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.45.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.1...n8n@1.45.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-06


This release contains new features, node enhancements, and bug fixes.


For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.44.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.44.0...n8n@1.44.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-06-03

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.44.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.43.1...n8n@1.44.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-30



This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.43.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.43.0...n8n@1.43.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-28

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.43.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.1...n8n@1.43.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-22


This release contains new features, node enhancements, and bug fixes.

/// note | Backup recommended
Although this release doesn't include a breaking change, it is a significant update including database migrations. n8n recommends backing up your data before updating to this version.
///

/// Note | Credential sharing required for manual executions
Instance owners and admins: you will see changes if you try to manually execute a workflow where the credentials aren't shared with you. Manual workflow executions now use the same permissions checks as production executions, meaning you can't do a manual execution of a workflow if you don't have access to the credentials. Previously, owners and admins could do manual executions without credentials being shared with them. To resolve this, the credential creator needs to [share the credential](/credentials/credential-sharing.md) with you.
///

<div class="n8n-new-features" markdown>

#### New feature: Projects

With projects and roles, you can give your team access to collections of workflows and credentials, rather than having to share each workflow and credential individually. Simultaneously, you tighten security by limiting access to people on the relevant team.
<br /><br />
Refer to the [RBAC](/user-management/rbac/index.md) documentation for information on creating projects and using roles.
<br /><br />
The number of projects and role types vary depending on your plan. Refer to [Pricing](https://n8n.io/pricing/){:target=_blank .external-link} for details.

<video src="/_video/release-notes/rbac-glimpse.mp4" controls width="100%"></video>

</div>

<div class="n8n-new-features" markdown>

#### New node: Slack Trigger

This release adds a trigger node for Slack. Refer to the [Slack Trigger documentation](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) for details.

</div>

### Other highlights

* Improved [memory support for OpenAI assistants](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

### Rolling back to a previous version

If you update to this version, then decide you need to role back:

Self-hosted n8n:

1. Delete any RBAC projects you created.
2. Revert the database migrations using `n8n db:revert`.

Cloud: contact [help@n8n.io](mailto:help@n8n.io).

### Contributors

[Ayato Hayashi](https://github.com/hayashi-ay){:target=_blank .external-link}  
[Daniil Zobov](https://github.com/ddzobov){:target=_blank .external-link}  
[Guilherme Barile](https://github.com/GuilhermeBarile){:target=_blank .external-link}  
[Romain MARTINEAU](https://github.com/RJiraya){:target=_blank .external-link}



## n8n@1.42.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.42.0...n8n@1.42.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-20


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.41.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.41.0...n8n@1.41.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-16



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.42.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.41.0...n8n@1.42.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-15



This release contains new features, node enhancements, and bug fixes.

Note that this release removes the AI error debugger. We're working on a new and improved version.

<div class="n8n-new-features" markdown>

#### New feature: Tools Agent

This release adds a new option to the Agent node: the [Tools Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md).

This agent has an enhanced ability to work with tools, and can ensure a standard output format. This is now the recommended default agent.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Mike Quinlan](https://github.com/mjquinlan2000){:target=_blank .external-link}  
[guangwu](https://github.com/testwill){:target=_blank .external-link}

## n8n@1.41.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.40.0...n8n@1.41.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-08


This release contains new features, node enhancements, and bug fixes.

Note that this release temporarily disables the AI error helper.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Florin Lungu](https://github.com/floryn90){:target=_blank .external-link}

## n8n@1.40.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.39.1...n8n@1.40.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-05-02

/// warning | Breaking change
Please note that this version contains a breaking change for instances using a Postgres database. The default value for the DB_POSTGRESDB_USER environment variable was switched from `root` to `postgres`. Refer to the [breaking changes log](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1400){:target=_blank .external-link} for details.
///

This release contains new features, new nodes, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### New feature: Ask AI in the HTTP node

You can now ask AI to help create API requests in the HTTP Request node:

1. In the HTTP Request node, select **Ask AI**.
1. Enter the **Service** and **Request** you want to use. For example, to use the NASA API to get their picture of the day, enter `NASA` in **Service** and `get picture of the day` in **Request**.
1. Check the parameters: the AI tries to fill them out, but you may still need to adjust or correct the configuration.

Self-hosted users need to [enable AI features and provide their own API keys](/hosting/configuration/environment-variables/index.md)

</div>

<div class="n8n-new-features" markdown>

#### New node: Groq Chat Model

This release adds the [Groq Chat Model node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Alberto Pasqualetto](https://github.com/albertopasqualetto){:target=_blank .external-link}  
[Bram Kn](https://github.com/bramkn){:target=_blank .external-link}  
[CodeShakingSheep](https://github.com/CodeShakingSheep){:target=_blank .external-link}  
[Nicolas-nwb](https://github.com/Nicolas-nwb){:target=_blank .external-link}  
[pemontto](https://github.com/pemontto){:target=_blank .external-link}  
[pengqiseven](https://github.com/pengqiseven){:target=_blank .external-link}  
[webk](https://github.com/webkp){:target=_blank .external-link}  
[Yoshino-s](https://github.com/Yoshino-s){:target=_blank .external-link}


## n8n@1.39.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.39.0...n8n@1.39.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-25



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.38.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.1...n8n@1.38.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-25



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.37.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.3...n8n@1.37.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-25

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.39.0


View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.1...n8n@1.39.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-24

This release contains new nodes, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: WhatsApp Trigger

This release adds the [WhatsApp Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md).

</div>

<div class="n8n-new-features" markdown>

#### Node enhancement: Multiple methods, one Webhook node

The Webhook Trigger node can now handle calls to multiple HTTP methods. Refer to the [Webhook node documentation](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md#listen-for-multiple-http-methods) for information on enabling this.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Bram Kn](https://github.com/bramkn){:target=_blank .external-link}

## n8n@1.38.1


View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.38.0...n8n@1.38.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-18

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.37.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.2...n8n@1.37.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-18



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.38.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.2...n8n@1.38.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-17

This release contains new nodes, bug fixes, and node enhancements.

<div class="n8n-new-features" markdown>

#### New node: Google Gemini Chat Model

This release adds the [Google Gemini Chat Model sub-node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Embeddings Google Gemini

This release adds the [Google Gemini Embeddings sub-node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Chengyou Liu](https://github.com/cyliu0){:target=_blank .external-link}  
[Francesco Mannino](https://github.com/manninofrancesco){:target=_blank .external-link}

## n8n@1.37.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.1...n8n@1.37.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.36.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.3...n8n@1.36.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-15

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.36.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.2...n8n@1.36.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-12

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.37.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.37.0...n8n@1.37.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-11


/// warning | Breaking change
Please note that this version contains a breaking change for self-hosted n8n. It removes the `--file` flag for the `execute` CLI command. If you have scripts relying on the `--file` flag, update them to first import the workflow and then execute it using the `--id` flag. Refer to [CLI commands](/hosting/cli-commands.md) for more information on CLI options.
///

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.36.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.1...n8n@1.36.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-11

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.37.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.1...n8n@1.37.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-10


/// warning | Breaking change
Please note that this version contains a breaking change for self-hosted n8n. It removes the `--file` flag for the `execute` CLI command. If you have scripts relying on the `--file` flag, update them to first import the workflow and then execute it using the `--id` flag. Refer to [CLI commands](/hosting/cli-commands.md) for more information on CLI options.
///

This release contains a new node, improvements to error handling and messaging, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: JWT

This release adds the [JWT core node](/integrations/builtin/core-nodes/n8n-nodes-base.jwt.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Miguel Prytoluk](https://github.com/mprytoluk){:target=_blank .external-link}

## n8n@1.36.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.36.0...n8n@1.36.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-04


This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.36.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.35.0...n8n@1.36.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-04-03

This release contains new nodes, enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: Salesforce Trigger node

This release adds the [Salesforce Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Twilio Trigger node

This release adds the [Twilio Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.35.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.2...n8n@1.35.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-28



This release contains enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.34.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.1...n8n@1.34.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-26



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.34.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.34.0...n8n@1.34.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-25



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.34.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.33.1...n8n@1.34.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-20

This release contains new features, new nodes, and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: Microsoft OneDrive Trigger node

This release adds the [Microsoft OneDrive Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md). You can now trigger workflows on file and folder creation and update events.

</div>

<div class="n8n-new-features" markdown>

#### New data transformation functions

This release introduces new [data transformation functions](/code/builtin/data-transformation-functions/index.md):

**String**

```js
toDateTime() //replaces toDate(). toDate() is retained for backwards compatability.
parseJson()
extractUrlPath()
toBoolean()
base64Encode()
base64Decode()
```

**Number**

```js
toDateTime()
toBoolean()
```

**Object**

```js
toJsonString()
```

**Array**

```js
toJsonString()
```

**Date & DateTime**

```js
toDateTime()
toInt()
```

**Boolean**

```js
toInt()
```

</div>

### Contributors

[Bram Kn](https://github.com/bramkn){:target=_blank .external-link}  
[pemontto](https://github.com/pemontto){:target=_blank .external-link}

## n8n@1.33.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.33.0...n8n@1.33.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-15



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.32.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.1...n8n@1.32.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-15





This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.33.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.1...n8n@1.33.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-13

This release contains new features, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### Support for Claude 3

This release adds support for Claude 3 to the [Anthropic Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md) node.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[gumida](https://github.com/gumida){:target=_blank .external-link}  
[Ayato Hayashi](https://github.com/hayashi-ay){:target=_blank .external-link}  
[Jordan](https://github.com/jordanburke){:target=_blank .external-link}  
[MC Naveen](https://github.com/mcnaveen){:target=_blank .external-link}

## n8n@1.32.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.32.0...n8n@1.32.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-07



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.31.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.1...n8n@1.31.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-07


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.32.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.1...n8n@1.32.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-06

This release contains new features, node enhancements, performance improvements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.31.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.31.0...n8n@1.31.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-03-06

/// warning | Breaking changes
Please note that this version contains a breaking change. HTTP connections to the editor will fail on domains other than localhost. You can read more about it [here](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#1320){:target=_blank .external-link}.
///

This is a bug fix release and it contains a breaking change.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.31.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.30.0...n8n@1.31.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-28

This release contains new features, new nodes, node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### New nodes: Microsoft Outlook trigger and Ollama embeddings

This release adds two new nodes.

* [Microsoft Outlook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)
* [Ollama Embeddings](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md)

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.30.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.30.0...n8n@1.30.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-23



This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.30.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.29.1...n8n@1.30.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-21





This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.29.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.29.0...n8n@1.29.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-16











This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.29.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.28.0...n8n@1.29.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-15

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### New features

<div class="n8n-new-features" markdown>

#### OpenAI node overhaul

This release includes a new version of the [OpenAI node](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md), adding more operations, including support for working with assistants.

</div>

Other highlights:

* Support for AI events in [log streaming](/log-streaming.md).
* Added support for workflow tags in the [public API](/api/index.md).

### Contributors

[Bruno Inec](https://github.com/sweenu){:target=_blank .external-link}  
[Jesús Burgers](https://github.com/jburgers-chakray){:target=_blank .external-link}

## n8n@1.27.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.2...n8n@1.27.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-15







This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.28.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.2...n8n@1.28.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-07



This release contains new features, new nodes, node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### New nodes: Azure OpenAI chat model and embeddings

This release adds two new nodes to work with [Azure OpenAI](https://azure.microsoft.com/en-gb/products/ai-services/openai-service/){:target=_blank .external-link} in your advanced AI workflows:

* [Embeddings Azure OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md)
* [Azure OpenAI Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Andrea Ascari](https://github.com/ascariandrea){:target=_blank .external-link}

## n8n@1.27.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.27.1...n8n@1.27.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-02-02

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.27.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.26.0...n8n@1.27.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-31

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.27.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.26.0...n8n@1.27.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-31

/// warning | Breaking change
This release removes `own` mode for self-hosted n8n. You must now use `EXECUTIONS_MODE` and set to either `regular` or `queue`. Refer to [Queue mode](/hosting/scaling/queue-mode.md) for information on configuring queue mode.
///

/// note | Skip this release
Please upgrade directly to 1.27.1.
///

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.26.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.25.1...n8n@1.26.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-24

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Daniel Schröder](https://github.com/schroedan){:target=_blank .external-link}  
[Nihaal Sangha](https://github.com/nihaals){:target=_blank .external-link}

## n8n@1.25.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.25.0...n8n@1.25.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-22

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Nihaal Sangha](https://github.com/nihaals){:target=_blank .external-link}

## n8n@1.25.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.24.1...n8n@1.25.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-17

This release contains a new node, feature improvements, and bug fixes.

<div class="n8n-new-features" markdown>

#### New node: Chat Memory Manager

The [Chat Memory Manager](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) node replaces the Chat Messages Retriever node. It manages chat message memories within your AI workflows.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.24.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.24.0...n8n@1.24.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-16

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.22.6

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.5...n8n@1.22.6){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-10

This is a bug fix release. It includes important fixes for the HTTP Request and monday.com nodes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.24.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.23.0...n8n@1.24.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-10


This release contains new nodes for advanced AI, node enhancements, new features, performance enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### Chat trigger

n8n has created a new [Chat Trigger node](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md). The new node provides a chat interface that you can make publicly available, with customization and authentication options.

</div>

<div class="n8n-new-features" markdown>

#### Mistral Cloud Chat and Embeddings

This release introduces two new nodes to support [Mistral AI](https://mistral.ai/){:target=_blank .external-link}:

* [Mistral Cloud Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Embeddings Mistral Cloud](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)

</div>

### Contributors

[Anush](https://github.com/Anush008){:target=_blank .external-link}  
[Eric Koleda](https://github.com/ekoleda-codaio){:target=_blank .external-link}  
[Mason Geloso](https://github.com/MasonGeloso){:target=_blank .external-link}  
[vacitbaydarman](https://github.com/vacitbaydarman){:target=_blank .external-link}

## n8n@1.22.5

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.4...n8n@1.22.5){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-09

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.



## n8n@1.23.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.4...n8n@1.23.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-03

This release contains new nodes, node enhancements, new features, and bug fixes.

<div class="n8n-new-features" markdown>

#### New nodes and improved experience for working with files

This release includes a major overhaul of nodes relating to files (binary data).

There are now three key nodes dedicated to handling binary data files:

- [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) to read and write files from/to the machine where n8n is running.
- [Convert to File](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) to take input data and output it as a file.
- [Extract From File](/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) to get data from a binary format and convert it to JSON.

n8n has moved support for iCalendar, PDF, and spreadsheet formats into these nodes, and removed the iCalendar, Read PDF, and Spreadsheet File nodes. There are still standalone nodes for [HTML](/integrations/builtin/core-nodes/n8n-nodes-base.html.md) and [XML](/integrations/builtin/core-nodes/n8n-nodes-base.xml.md).

</div>

<div class="n8n-new-features" markdown>

#### New node: Qdrant vector store

This release adds support for [Qdrant](https://qdrant.tech/){:target=_blank .external-link} with the Qdrant vector store node.

Read n8n's [Qdrant vector store node documentation](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)

</div>

### Contributors



[Aaron Gutierrez](https://github.com/aarongut){:target=_blank .external-link}  
[Advaith Gundu](https://github.com/geodic){:target=_blank .external-link}  
[Anush](https://github.com/Anush008){:target=_blank .external-link}  
[Bin](https://github.com/soulhat){:target=_blank .external-link}  
[Nihaal Sangha](https://github.com/nihaals){:target=_blank .external-link}



## n8n@1.22.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.3...n8n@1.22.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2024-01-03



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.22.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.2...n8n@1.22.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-27

/// note | Upgrade directly to 1.22.4
Due to issues with this release, upgrade directly to 1.22.4.
///

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.22.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.1...n8n@1.22.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-27

/// note | Upgrade directly to 1.22.4
Due to issues with this release, upgrade directly to 1.22.4.
///

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.22.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.22.0...n8n@1.22.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-21

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.22.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.21.1...n8n@1.22.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-21

This release contains node enhancements, new features, performance improvements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.18.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.3...n8n@1.18.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-19

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.21.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.20.0...n8n@1.21.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-15



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.18.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.2...n8n@1.18.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-15

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.21.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.20.0...n8n@1.21.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-13

This release contains new features and nodes, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### New user role: Admin

This release introduces a third account type: admin. This role is available on pro and enterprise plans. Admins have similar permissions to instance owners.

[Read more about user roles](/user-management/account-types.md)

</div>

<div class="n8n-new-features" markdown>

#### New data transformation nodes

This release replaces the Item Lists node with a collection of nodes for data transformation tasks:

* [Aggregate](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): take separate items, or portions of them, and group them together into individual items.
* [Limit](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): remove items beyond a defined maximum number.
* [Remove Duplicates](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md): identify and delete items that are identical across all fields or a subset of fields.
* [Sort](/integrations/builtin/core-nodes/n8n-nodes-base.sort.md): organize lists of in a desired ordering, or generate a random selection.
* [Split Out](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md): separate a single data item containing a list into multiple items.
* [Summarize](/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md): aggregate items together, in a manner similar to Excel pivot tables.

</div>

<div class="n8n-new-features" markdown>

#### Increased sharing permissions for owners and admins

Instance owners and users with the admin role can now see and share all workflows and credentials. They can't view sensitive credential information.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.20.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.5...n8n@1.20.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-06

This release contains bug fixes, node enhancements, and ongoing new feature work.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors


[Andrey Starostin](https://github.com/mayorandrew){:target=_blank .external-link}



## n8n@1.19.5

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.4...n8n@1.19.5){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-05

This is a bug fix release.

/// warning | Breaking change
This release removes the TensorFlow Embeddings node.
///

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.18.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.1...n8n@1.18.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-05

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.19.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.19.0...n8n@1.19.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-12-01

/// warning | Missing ARM v7 support
This version doesn't support ARM v7. n8n is working on fixing this in future releases.
///

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.19.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.0...n8n@1.19.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-29

/// note | Upgrade directly to 1.19.4
Due to issues with this release, upgrade directly to 1.19.4.
///

This release contains new features, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### LangChain general availability

This release adds LangChain support to the main n8n version. Refer to [LangChain](/advanced-ai/langchain/overview.md) for more information on how to build AI tools in n8n, the new nodes n8n has introduced, and related learning resources.

</div>

<div class="n8n-new-features" markdown>

#### Show avatars of users working on the same workflow

This release improves the experience of users collaborating on workflows. You can now see who else is editing at the same time as you.

</div>

## n8n@1.18.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.18.0...n8n@1.18.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-30

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.18.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.17.1...n8n@1.18.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-22

This release contains new features and bug fixes.

<div class="n8n-new-features" markdown>

#### Template creator hub

Built a template you want to share? This release introduces the n8n Creator hub. Refer to the [creator hub Notion doc](https://www.notion.so/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f){:target=_blank .external-link} for more information on this project.

</div>

<div class="n8n-new-features" markdown>

#### Node input and output search filter

Cloud Pro and Enterprise users can now search and filter the input and output data in nodes. Refer to [Data filtering](/data/data-filtering.md) for more information.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.17.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.17.0...n8n@1.17.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-17

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.17.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.16.0...n8n@1.17.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-15



This release contains node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### Sticky Note Colors

You can now select background colors for sticky notes.

</div>

<div class="n8n-new-features" markdown>

#### Discord Node Overhaul

An overhaul of the Discord node, improving the UI making it easier to configure, improving error handling, and fixing issues.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors


[antondollmaier](https://github.com/antondollmaier){:target=_blank .external-link}  
[teomane](https://github.com/teomane){:target=_blank .external-link}

## n8n@1.16.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.15.2...n8n@1.16.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-08

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.15.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.15.1...n8n@1.15.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-07

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.15.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.2...n8n@1.15.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-11-02


This release contains new features, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### Workflow history

This release introduces workflow history: view and load previous versions of your workflows.

Workflow history is available in Enterprise n8n, and with limited history for Cloud Pro.

Learn more in the [Workflow history](/workflows/history.md) documentation.

</div>

<div class="n8n-new-features" markdown>

#### Dark mode

_Almost_ in time for Halloween: this release introduces dark mode.

To enable dark mode:

1. Select **Settings** > **Personal**.
1. Under **Personalisation**, change **Theme** to **Dark theme**.

</div>

<div class="n8n-new-features" markdown>

#### Optional error output for nodes

All nodes apart from sub-nodes and trigger nodes have a new optional output: **Error**. Use this to add steps to handle node errors.

</div>

<div class="n8n-new-features" markdown>

#### Pagination support added to HTTP Request node

The HTTP Request node now supports an pagination. Read the [node docs](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) for information and examples.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Yoshino-s](https://github.com/Yoshino-s){:target=_blank .external-link}

## n8n@1.14.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.1...n8n@1.14.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.14.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.14.0...n8n@1.14.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-26

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.14.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.13.0...n8n@1.14.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-25

This release contains node enhancements and bug fixes.

<div class="n8n-new-features" markdown>

#### Switch node supports more outputs

The [Switch node](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) now supports an unlimited number of outputs.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.13.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.2...n8n@1.13.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-25

This release contains new features, feature enhancements, and bug fixes.

/// note | Upgrade directly to 1.14.0
This release failed to publish to npm. Upgrade directly to 1.14.0.
///
<div class="n8n-new-features" markdown>

#### RSS Feed Trigger node

This releases introduces a new node, the [RSS Feed Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md). Use this node to start a workflow when a new RSS feed item is published.

</div>

<div class="n8n-new-features" markdown>

#### Facebook Lead Ads Trigger node

This releases add another new node, the [Facebook Lead Ads Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md). Use this node to trigger a workflow when you get a new lead.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.12.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.1...n8n@1.12.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-24


This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Burak Akgün](https://github.com/mbakgun){:target=_blank .external-link}

## n8n@1.12.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.12.0...n8n@1.12.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-23


This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Léo Martinez](https://github.com/martinezleoml){:target=_blank .external-link}

## n8n@1.11.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.1...n8n@1.11.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-23

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Inga](https://github.com/inga-lovinde){:target=_blank .external-link}  
[pemontto](https://github.com/pemontto){:target=_blank .external-link}

## n8n@1.12.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.1...n8n@1.12.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-18

This release contains new features, node enhancements, and bug fixes.

<div class="n8n-new-features" markdown>

#### Form Trigger node

This releases introduces a new node, the [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md). Use this node to start a workflow based on a user submitting a form. It provides a configurable form interface.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Damian Karzon](https://github.com/dkarzon){:target=_blank .external-link}  
[Inga](https://github.com/inga-lovinde){:target=_blank .external-link}  
[pemontto](https://github.com/pemontto){:target=_blank .external-link}


## n8n@1.11.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.11.0...n8n@1.11.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-13

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.11.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.10.1...n8n@1.11.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-11


This release contains new features and bug fixes.

<div class="n8n-new-features" markdown>

#### External storage for binary files

Self-hosted users can now use an external service to store binary data. Learn more in [External storage](/hosting/scaling/external-storage.md).

If you're using n8n Cloud and are interested in this feature, please [contact n8n](https://n8n-community.typeform.com/to/y9X2YuGa){:target=_blank .external-link}.

</div>

<div class="n8n-new-features" markdown>

#### Item Lists node supports binary data

The Item Lists node now supports splitting and concatenating binary data inputs. This means you no longer need to use code to split a collection of files into multiple items.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.10.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.10.0...n8n@1.10.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-11

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.9.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.2...n8n@1.9.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-10

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.9.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.1...n8n@1.9.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-09

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.10.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.1...n8n@1.10.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-05



This release contains bug fixes and preparatory work for new features.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.9.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.9.0...n8n@1.9.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-10-04

This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## LangChain in n8n (beta)

**Release date:** 2023-10-04

This release introduces support for building with LangChain in n8n.

With n8n's LangChain nodes you can build AI-powered functionality within your workflows. The LangChain nodes are configurable, meaning you can choose your preferred agent, LLM, memory, and other components. Alongside the LangChain nodes, you can connect any n8n node as normal: this means you can integrate your LangChain logic with other data sources and services.

Read more:

* This is a beta release, and not yet available in the main product. Follow the instructions in [Access LangChain in n8n](/advanced-ai/langchain/overview.md) to try it out. Self-hosted and Cloud options are available.
* Learn how LangChain concepts map to n8n nodes in [LangChain concepts in n8n](/advanced-ai/langchain/langchain-n8n.md).
* Browse n8n's new [Cluster nodes](/integrations/builtin/cluster-nodes/index.md). This is a new set of node types that allows for multiple nodes to work together to configure each other.

## n8n@1.9.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.2...n8n@1.9.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-28


This release contains new features, performance improvements, and bug fixes.

<div class="n8n-new-features" markdown>

#### Tournament

This releases replaces RiotTmpl, the templating language used in expressions, with n8n's own templating language, [Tournament](https://github.com/n8n-io/tournament){:target=_blank .external-linmk}. You can now use arrow functions in expressions.<br />

</div>

<div class="n8n-new-features" markdown>

#### `N8N_BINARY_DATA_TTL` and `EXECUTIONS_DATA_PRUNE_TIMEOUT` removed

The environment variables `N8N_BINARY_DATA_TTL` and `EXECUTIONS_DATA_PRUNE_TIMEOUT` no longer have any effect and can be removed. Instead of relying on a TTL system for binary data, n8n cleans up binary data together with executions during pruning.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.8.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.1...n8n@1.8.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-25




This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.8.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.8.0...n8n@1.8.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-21


This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.8.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.7.1...n8n@1.8.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-20

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.7.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.7.0...n8n@1.7.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-14


This release contains bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.7.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.6.1...n8n@1.7.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-13

This release contains node enhancements and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Quang-Linh LE](https://github.com/linktohack){:target=_blank .external-link}  
[MC Naveen](https://github.com/mcnaveen){:target=_blank .external-link}

## n8n@1.6.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.6.0...n8n@1.6.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-06


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.6.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.5.1...n8n@1.6.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-09-06

This release contains bug fixes, new features, and node enhancements.

/// note | Upgrade directly to 1.6.1
Skip this version and upgrade directly to 1.6.1, which contains essential bug fixes.
///
<div class="n8n-new-features" markdown>

#### TheHive 5

This release introduces support for TheHive API version 5. This uses a new node and credentials:

* [TheHive 5 node](/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md)
* [TheHive 5 Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md)
* [TheHive 5 credentials](/integrations/builtin/credentials/thehive5.md)

#### `N8N_PERSISTED_BINARY_DATA_TTL` removed

The environment variables `N8N_PERSISTED_BINARY_DATA_TTL` no longer has any effect and can be removed. This legacy flag was originally introduced to support ephemeral executions (see [details](https://github.com/n8n-io/n8n/pull/7046)), which are no longer supported.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.5.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.5.0...n8n@1.5.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-31


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.5.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.4.1...n8n@1.5.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-31

This release contains new features, node enhancements, and bug fixes.

/// note | Upgrade directly to 1.5.1
Skip this version and upgrade directly to 1.5.1, which contains essential bug fixes.
///
### Highlights

<div class="n8n-new-features" markdown>

#### External secrets storage for credentials

Enterprise-tier accounts can now use external secrets vaults to manage credentials in n8n. This allows you to store credential information securely outside your n8n instance. n8n supports Infisical and HashiCorp Vault.

Refer to [External secrets](/external-secrets.md) for guidance on enabling and using this feature.

</div>

<div class="n8n-new-features" markdown>

#### Two-factor authentication

n8n now supports two-factor authentication (2FA) for self-hosted instances. n8n is working on bringing support to Cloud. Refer to [Two-factor authentication](/user-management/two-factor-auth.md) for guidance on enabling and using it.

</div>

<div class="n8n-new-features" markdown>

#### Debug executions

Users on a paid n8n plan can now load data from previous executions into their current workflow. This is useful when debugging a failed execution.

Refer to [Debug executions](/workflows/executions/debug.md) for guidance on using this feature.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.4.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.4.0...n8n@1.4.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-29



This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.4.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.3.1...n8n@1.4.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-23

This release contains new features, node enhancements, and bug fixes.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[pemontto](https://github.com/pemontto){:target=_blank .external-link}

## n8n@1.3.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.3.0...n8n@1.3.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-18

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.


## n8n@1.3.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.2...n8n@1.3.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-16

This release contains new features and bug fixes.

### Highlights

<div class="n8n-new-features" markdown>

#### Trial feature: AI support in the Code node

This release introduces limited support for using AI to generate code in the Code node. Initially this feature is only available on Cloud, and will gradually be rolled out, starting with about 20% of users.

Learn how to use the feature, including guidance on writing prompts, in [Generate code with ChatGPT](/code/ai-code.md).

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Ian Gallagher](https://github.com/craSH){:target=_blank .external-link}  
[Xavier Calland](https://github.com/xavier-calland){:target=_blank .external-link}

## n8n@1.2.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.1...n8n@1.2.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-14

This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.2.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.2.0...n8n@1.2.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-09


This is a bug fix release.

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.2.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.1.1...n8n@1.2.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-08-09

This release contains new features, node enhancements, bug fixes, and performance improvements.

/// note | Upgrade directly to 1.2.1
When upgrading, skip this release and go directly to 1.2.1.
///
### Highlights

<div class="n8n-new-features" markdown>

#### Credential support for SecOps services

This release introduces support for setting up credentials in n8n for the following services:

* [AlienVault](/integrations/builtin/credentials/alienvault.md)
* [Auth0 Management](/integrations/builtin/credentials/auth0management.md)
* [Carbon Black API](/integrations/builtin/credentials/carbonblack.md)
* [Cisco Meraki API](/integrations/builtin/credentials/ciscomeraki.md)
* [Cisco Secure Endpoint](/integrations/builtin/credentials/ciscosecureendpoint.md)
* [Cisco Umbrella API](/integrations/builtin/credentials/ciscoumbrella.md)
* [CrowdStrike](/integrations/builtin/credentials/crowdstrike.md)
* [F5 Big-IP](/integrations/builtin/credentials/f5bigip.md)
* [Fortinet FortiGate](/integrations/builtin/credentials/fortigate.md)
* [Hybrid Analysis](/integrations/builtin/credentials/hybridanalysis.md)
* [Imperva WAF](/integrations/builtin/credentials/impervawaf.md)
* [Kibana](/integrations/builtin/credentials/kibana.md)
* [Microsoft Entra ID](/integrations/builtin/credentials/microsoftentra.md)
* [Mist](/integrations/builtin/credentials/mist.md)
* [Okta](/integrations/builtin/credentials/okta.md)
* [OpenCTI](/integrations/builtin/credentials/opencti.md)
* [QRadar](/integrations/builtin/credentials/qradar.md)
* [Qualys](/integrations/builtin/credentials/qualys.md)
* [Recorded Future](/integrations/builtin/credentials/recordedfuture.md)
* [Sekoia](/integrations/builtin/credentials/sekoia.md)
* [Shuffler](/integrations/builtin/credentials/shuffler.md)
* [Trellix ePO](/integrations/builtin/credentials/trellixepo.md)
* [VirusTotal](/integrations/builtin/credentials/virustotal.md)
* [Zscaler ZIA](/integrations/builtin/credentials/zscalerzia.md)

This makes it easier to do [Custom operations](/integrations/custom-operations.md) with these services, using the [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.1.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.1.0...n8n@1.1.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-27


This is a bug fix release.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.1.0

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.5...n8n@1.1.0){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-26

This release contains new features, bug fixes, and node enhancements.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
### Highlights

<div class="n8n-new-features" markdown>

#### Source control and environments

This release introduces source control and environments for enterprise users.

n8n uses Git-based source control to support environments. Linking your n8n instances to a Git repository lets you create multiple n8n environments, backed by Git branches.

Refer to [Source control and environments](/source-control-environments/index.md) to learn more about the features and set up your environments.

</div>

For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Adrián Martínez](https://github.com/adrian-martinez-vdshop){:target=_blank .external-link}  
[Alberto Pasqualetto](https://github.com/albertopasqualetto){:target=_blank .external-link}  
[Marten Steketee](https://github.com/Marten-S){:target=_blank .external-link}  
[perseus-algol](https://github.com/perseus-algol){:target=_blank .external-link}  
[Sandra Ashipala](https://github.com/sandramsc){:target=_blank .external-link}  
[ZergRael](https://github.com/ZergRael){:target=_blank .external-link}

## n8n@1.0.5

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.4...n8n@1.0.5){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-24



This is a bug fix release.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

## n8n@1.0.4

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.3...n8n@1.0.4){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-19


This is a bug fix release.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Romain Dunand](https://github.com/airmoi){:target=_blank .external-link}  
[noctarius aka Christoph Engelbert](https://github.com/noctarius){:target=_blank .external-link}


## n8n@1.0.3

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.2...n8n@1.0.3){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-13

This release contains API enhancements and adds support for sending messages to forum threads in the Telegram node.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
For full release details, refer to [Releases](https://github.com/n8n-io/n8n/releases){:target=_blank .external-link} on GitHub.

### Contributors

[Kirill](https://github.com/chrtkv){:target=_blank .external-link}

## n8n@1.0.2

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.1...n8n@1.0.2){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-05

This is a bug fix release.

/// warning | Breaking changes
Please note that this version contains breaking changes if upgrading from a `0.x.x` version. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
### Contributors

[Romain Dunand](https://github.com/airmoi){:target=_blank .external-link}

## n8n@1.0.1

View the [commits](https://github.com/n8n-io/n8n/compare/n8n@1.0.0...n8n@1.0.1){:target=_blank .external-link} for this version.<br />
**Release date:** 2023-07-05

/// warning | Breaking changes
Please note that this version contains breaking changes. For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).
///
This is n8n's version one release.

For full details, refer to the [n8n v1.0 migration guide](/1-0-migration-checklist.md).

### Highlights

<div class="n8n-new-features" markdown>

#### Python support

Although JavaScript remains the default language, you can now also select Python as an option in the [Code node](/code/code-node.md) and even make use of [many Python modules](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide){:target=_blank .external link}. Note that Python is unavailable in Code nodes added to a workflow before v1.0.

</div>

### Contributors

[Marten Steketee](https://github.com/Marten-S){:target=_blank .external-link}

<!-- vale on -->


---

<!-- Source: docs/sustainable-use-license.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Sustainable Use License
description: The n8n Sustainable Use License.
contentType: explanation
---

<!-- vale off -->

# Sustainable Use License

/// note | Proprietary licenses for Enterprise
Proprietary licenses are available for enterprise customers. [Get in touch](mailto:license@n8n.io) for more information.
///

n8n's [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md){:target=\_blank .external-link} and [n8n Enterprise License](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md){:target=\_blank .external-link} are based on the [fair-code](https://faircode.io/) model.

## License FAQs

### What license do you use?

n8n uses the [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) and [n8n Enterprise License](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md){:target=_blank .external-link}. These licenses are based on the [fair-code](https://faircode.io/) model.


### What source code is covered by the Sustainable Use License? 

The [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) applies to all our source code hosted in our [main GitHub repository](https://github.com/n8n-io/n8n) except:

* Content of branches other than master.
* Source code files that contain `.ee.` in their file name. These are licensed under the [n8n Enterprise License](https://github.com/n8n-io/n8n/blob/master/LICENSE_EE.md){:target=_blank .external-link}.

### What is the Sustainable Use License?

The Sustainable Use License is a fair-code software license created by n8n in 2022. You can read more about why we did this [here](#why-did-you-create-a-license). The license allows you the free right to use, modify, create derivative works, and redistribute, with three limitations:

* You may use or modify the software only for your own internal business purposes or for non-commercial or personal use.
* You may distribute the software or provide it to others only if you do so free of charge for non-commercial purposes.
* You may not alter, remove, or obscure any licensing, copyright, or other notices of the licensor in the software. Any use of the licensor's trademarks is subject to applicable law.

We encourage anyone who wants to use the Sustainable Use License. If you are building something out in the open, it makes sense to think about licensing earlier in order to avoid problems later. Contact us at [license@n8n.io](mailto:license@n8n.io) if you would like to ask any questions about it. 


### What is and isn't allowed under the license in the context of n8n's product?

Our license restricts use to "internal business purposes". In practice this means all use is allowed unless you are selling a product, service, or module in which the value derives entirely or substantially from n8n functionality. Here are some examples that wouldn't be allowed:

* White-labeling n8n and offering it to your customers for money.
* Hosting n8n and charging people money to access it.

All of the following examples are allowed under our license: 

* Using n8n to sync the data you control as a company, for example from a CRM to an internal database.
* Creating an n8n node for your product or any other integration between your product and n8n.
* Providing consulting services related to n8n, for example building workflows, custom features closely connect to n8n, or code that gets executed by n8n.
* Supporting n8n, for example by setting it up or maintaining it on an internal company server.

#### Can I use n8n to act as the back-end to power a feature in my app?

Usually yes, as long as the back-end process doesn't use users' own credentials to access their data.

Here are two examples to clarify:

##### Example 1: Sync ACME app with HubSpot

Bob sets up n8n to collect a user's HubSpot credentials to sync data in the ACME app with data in HubSpot.

<span style="color: #BF2F51;">**NOT ALLOWED**</span> under the Sustainable Use License. This use case collects the user's own HubSpot credentials to pull information to feed into the ACME app.

##### Example 2: Embed AI chatbot in ACME app

Bob sets up n8n to embed an AI chatbot within the ACME app. The AI chatbot's credentials in n8n use Bob's company credentials. ACME app end-users only enter their questions or queries to the chatbot.

<span style="color: #1C9985;">**ALLOWED**</span> under the Sustainable Use License. No user credentials are being collected.

### What if I want to use n8n for something that's not permitted by the license?

You must sign a separate commercial agreement with us. We actively encourage software creators to embed n8n within their products; we just ask them to sign an agreement laying out the terms of use, and the fees owed to n8n for using the product in this way. We call this mode of use n8n Embed. You can learn more, and contact us about it [here](https://n8n.io/embed). 

If you are unsure whether the use case you have in mind constitutes an internal business purpose or not, take a look at [the examples](#what-is-and-isnt-allowed-under-the-license-in-the-context-of-n8ns-product), and if you're still unclear, email us at [license@n8n.io](mailto:license@n8n.io).

### Why don't you use an open source license?

n8n's mission is to give everyone who uses a computer technical superpowers. We've decided the best way for us to achieve this mission is to make n8n as widely and freely available as possible for users, while ensuring we can build a sustainable, viable business. By making our product free to use, easy to distribute, and source-available we help everyone access the product. By operating as a business, we can continue to release features, fix bugs, and provide reliable software at scale long-term.

### Why did you create a license?

Creating a license was our least favorite option. We only went down this path after reviewing the possible existing licenses and deciding nothing fit our specific needs. There are two ways in which we try to mitigate the pain and friction of using a proprietary license:

1. By using plain English, and keeping it as short as possible.
2. By promoting [fair-code](https://faircode.io/) with the goal of making it a well-known umbrella term to describe software models like ours.

Our goals when we created the Sustainable Use License were:

1. To be as permissive as possible.
2. Safeguarding our ability to build a business.
3. Being as clear as possible what use was permitted or not.

### My company has a policy against using code that restricts commercial use – can I still use n8n?

Provided you are using n8n for internal business purposes, and not making n8n available to your customers for them to connect their accounts and build workflows, you should be able to use n8n. If you are unsure whether the use case you have in mind constitutes an internal business purpose or not, take a look at [the examples](#what-is-and-isnt-allowed-under-the-license-in-the-context-of-n8ns-product), and if you're still unclear, email us at [license@n8n.io](mailto:license@n8n.io).


### What happens to the code I contribute to n8n in light of the Sustainable Use License?

Any code you contribute on GitHub is subject to GitHub's [terms of use](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content). In simple terms, this means you own, and are responsible for, anything you contribute, but that you grant other GitHub users certain rights to use this code. When you contribute code to a repository containing notice of a license, you license the code under the same terms.

n8n asks every contributor to sign our [Contributor License Agreement](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTOR_LICENSE_AGREEMENT.md). In addition to the above, this gives n8n the ability to change its license without seeking additional permission. It also means you aren't liable for your contributions (e.g. in case they cause damage to someone else's business).

It's easy to get started contributing code to n8n [here](https://github.com/n8n-io), and we've listed broader ways of participating in our community [here](https://docs.n8n.io/reference/contributing.html).


### Why did you switch to the Sustainable Use License from your previous license arrangement (Apache 2.0 with Commons Clause)?

n8n was licensed under Apache 2.0 with Commons Clause until 17 March 2022. Commons Clause was initiated by various software companies wanting to protect their rights against cloud providers. The concept involved adding a commercial restriction on top of an existing open source license.

However, the use of the Commons Clause as an additional condition to an open source license, as well as the use of wording that's open to interpretation, created some confusion and uncertainty regarding the terms of use. The Commons Clause also restricted people's ability to offer consulting and support services: we realized these services are critical in enabling people to get value from n8n, so we wanted to remove this restriction.

We created the Sustainable Use License to be more permissive and more clear about what use is allowed, while continuing to ensure n8n gets the funding needed to build and improve our product.

### What are the main differences between the Sustainable Use License and your previous license arrangement (Apache 2.0 with Commons Clause)?

There are two main differences between the Sustainable Use License and our previous license arrangement. The first is that we have tightened the definition of how you can use the software. Previously the Commons Clause restricted users ability to "sell" the software; we have redefined this to restrict use to internal business purposes. The second difference is that our previous license restricted people's ability to charge fees for consulting or support services related to the software: we have lifted that restriction altogether.

That means you are now free to offer commercial consulting or support services (e.g. building n8n workflows) without the need for a separate license agreement with us. If you are interested in joining our community of n8n experts providing these services, you can learn more here.

### Is n8n open source?

Although n8n's source code is available under the Sustainable Use License, according to the [Open Source Initiative](https://opensource.org/) (OSI), open source licenses can't include limitations on use, so we do not call ourselves open source. In practice, n8n offers most users many of the same benefits as OSI-approved open source.

We coined the term ['fair-code'](https://faircode.io/) as a way of describing our licensing model, and the model of other companies who are source-available, but restrict commercial use of their source code.

### What is fair-code, and how does the Sustainable Use License relate to it?

Fair-code isn't a software license. It describes a software model where software:

* Is generally free to use and can be distributed by anybody.
* Has its source code openly available.
* Can be extended by anybody in public and private communities.
* Is commercially restricted by its authors.

The Sustainable Use License is a fair-code license. You can read more about it and see other examples of fair-code licenses [here](https://faircode.io/).

We're always excited to talk about software licenses, fair-code, and other principles around sharing code with interested parties. To get in touch to chat, email [license@n8n.io](mailto:license@n8n.io).

### Can I use n8n's Sustainable Use License for my own project?

Yes! We're excited to see more software use the Sustainable Use License. We'd love to hear about your project if you're using our license: [license@n8n.io](mailto:license@n8n.io).

<!-- vale on -->


---

<!-- Source: docs/video-courses.md -->

---

---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Video courses
description: Links to n8n's video courses on YouTube.
contentType: overview
---

# Video courses

n8n provides two video courses on YouTube.

For support, join the [Forum](https://community.n8n.io/){:target=_blank .external-link}.

## Beginner

The [Beginner](https://www.youtube.com/playlist?list=PLlET0GsrLUL59YbxstZE71WszP3pVnZfI){:target=_blank .external-link} course covers the basics of n8n:

- [Introduction and workflows](https://youtu.be/4BVTkqbn_tY?si=g2A5eD8kAoia5k6y){:target=_blank .external-link}
- [APIs and Webhooks](https://youtu.be/y_cpFMF1pzk?si=zi3wM4W7nx8Jkcw3){:target=_blank .external-link}
- [Nodes](https://youtu.be/rCPXBkeBWCQ?si=-T2iUsydwS5ym6yI){:target=_blank .external-link}
- [Data in n8n](https://youtu.be/2YfWuNziPE4?si=4jB-fubG1_T0HXYx){:target=_blank .external-link}
- [Core workflow concepts](https://youtu.be/kkrA7tGHYNo?si=mLVbuV98ohL5YVnm){:target=_blank .external-link}
- [Useful nodes](https://youtu.be/Rmi-ckbMOQE?si=H_dF77uf5KJU7RtH){:target=_blank .external-link}
- [Error handling](https://youtu.be/XEUVl3bbMhI?si=nUyaME5kyxe6daGO){:target=_blank .external-link}
- [Debugging](https://youtu.be/Gxe_RfCRH-o?si=F-pAviLTIeL3-X13){:target=_blank .external-link}
- [Collaboration](https://youtu.be/pI0W-0Qcwmo?si=X7sALFXo2e-cY9FQ){:target=_blank .external-link}


## Advanced

The [Advanced](https://www.youtube.com/playlist?list=PLlET0GsrLUL5bxmx5c1H1Ms_OtOPYZIEG){:target=_blank .external-link} course covers more complex workflows, more technical nodes, and enterprise features:

- [Introduction and complex data flows](https://youtu.be/TFTLMQLozCI?si=vX0ooIH1RmbsgAkC){:target=_blank .external-link}
- [Advanced technical nodes](https://youtu.be/JM4jqYs4Fxo?si=YSNMeSay3C29C8HS){:target=_blank .external-link}
- [Pinning and editing output data](https://youtu.be/zcNB8L4_9mA?si=LZJ9DlYDQQxL7eeP){:target=_blank .external-link}
- [Sub-workflows](https://youtu.be/xr05Ie_Hkyg?si=rqqP8llttZPBjBeD){:target=_blank .external-link}
- [Error workflows](https://youtu.be/77Ewdaby47M?si=6YRlC4nMgG4hVQPV){:target=_blank .external-link}
- [Building a full example](https://youtu.be/wOKLEfeJLVE?si=YMW5t-PzPq7QKbPY){:target=_blank .external-link}
- [Handling files](https://youtu.be/2RAZYNigqOY?si=9x4vLX2Qo08xx8vC){:target=_blank .external-link}
- [Enterprise features](https://youtu.be/fXEubzmVJ_E?si=aK9_fI9tkF6F5CtB){:target=_blank .external-link}
