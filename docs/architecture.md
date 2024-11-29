# Architecture

### Goals

Before we dig into the specific architecture we should discuss the guiding principles that impact our architecture.

Dos:

1. **Consistent** - Be predictable, using the same naming conventions  whenever possible
2. **Simple** - Most operation should only require 2-3 short lines of code.
3. **Pythonic** - API spec naming conventions should be made pythonic.
3. **Portable** - Architecture should be language agnostic
    * (+) Structs
    * (+) Functions
    * (+) Namespaces
    * (+) Composition
    * (-) Inheritance
    * (-) Polymorphism


Don'ts:

* **Verbosity**
    * Don't overwhelm users with complicated object and function names.
    * Avoid special casing shared concepts across different namespaces and contexts.
    * Avoid new object types when existing known objects would suffice (e.g., `dict`, `list`)

### client (Client)

Ideally, the `client` builder function is the only thing most users will need to import.
This function should handle constructing the necessary `Config`, `Auth` and `Session` objects used
to instantiate the `Client` for the requested service name (e.g., `clusters`, `vpcs`, `servers/virtual`).

Each service currently has an autogenerated `Client` class which wraps a `Session` object and provides methods for all the included paths (e.g., `GetAll`, `CreateServer`).

NOTES:

- All function and argument names are converted to the more pythonic snakecase format (e.g., `GetAll` -> `get_all`, `vpcId` -> `vpc_id`)
- We currently gatekeep which paths are include in our `scripts/apigen.py` file.
- Composition over inheritance as that seemed easier to implement across languages.
  - We're passing a shared `Session` object into each generated independent `Client` object rather than having shared logic in an `AbstractClient` parent.
- Namespacing over unique object names
  - Rather than having complicated names you should be able to just load the service you care about
  - We don't wrap method input / outputs in custom object types since folks already know how `list`, `dict`, etc work.

### Session

The Session object wraps all API requests calls, including any config defaults and passing the `Auth` object.
The goal of this object is limit the complexity of the generated `Client` objects for each service.

NOTES:

- All requests have the content type set to "application/json"`
- Any common error handling occurs in one place
- We just auto-extract the `json` and return the `results` item.

### Config

The config handles loading values from `~/.config/denvr.toml`, or the location of the `DENVR_CONFIG` environment variable.
An `Auth` object is created from either:

- `DENVR_USERNAME` and `DENVR_PASSWOR`
- The `username` and `password` values in the `credentials` section of the `denvr.toml` file.

### Auth

An object for handling requesting and refreshing access tokens given an initial username and password.
It is callable and subtypes `requests.auth.AuthBase` so that we can pass it as the `auth` keyword to `requests`

NOTE: The password isn't stored in the object and will be deleted when it goes out of scope in the `Auth` and `Config` constructors.