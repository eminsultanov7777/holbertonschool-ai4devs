Risk Assessment --- WordPress Core
Project: WordPress Core
Repository: WordPress/wordpress-develop
Assessment date: November 16, 2026
Scope and assessment notes
This assessment focuses on architectural and maintenance risks in the
WordPress Core areas reviewed in ai_explanations.md: content queries,
post creation and updates, capability mapping, nonce verification, and
HTML filtering.

Severity reflects the potential impact if the risk is introduced or
handled incorrectly. These are risk areas to review, not claims that
an exploitable vulnerability or active defect has been confirmed in the
current WordPress release.
Risk Assessment Table
  ID             Risk                     Severity       Affected area              Notes / potential
impact
  R1             Incorrect authorization  High           map_meta_cap(),          Developers may
checks in custom code                   capability APIs            confuse capability
mapping with a
completed
permission
decision, or check
role names instead
of object-specific
capabilities. This
can result in
unauthorized access
if calling code
does not perform
the correct
capability check.

  R2             Incorrect use of nonces  High           wp_verify_nonce() and    A valid nonce helps
as an authorization                     request handlers           verify request
mechanism                                                          intent and context,
but it does not
prove that a user
is authorized and
it is not a
one-time token.
Omitting a separate
capability check
can expose
privileged actions.

  R3             Unsafe handling of       High           wp_kses() and output     Overly permissive
user-supplied HTML                      handling                   allowlists or using
HTML sanitization
in the wrong output
context can allow
unsafe content or
create a false
sense of security.
Different contexts
such as HTML,
attributes,
JavaScript, and
URLs require
appropriate
handling.

  R4             Unexpected behavior      Medium         WP_Query::get_posts(),   Hooks and filters
caused by plugin and                    wp_insert_post()         allow extensions to
theme hooks                                                        alter queries and
post-save behavior.
A callback may
change data,
trigger extra
queries, or cause
side effects that
are difficult to
trace.

  R5             Performance degradation  Medium         WP_Query::get_posts()    Complex
from complex queries and                                           metadata/taxonomy
cache behavior                                                     queries, repeated
queries, or
ineffective caching
can increase
database load and
slow pages,
especially on sites
with large content
collections.

  R6             Regression risk when     High           wp_insert_post()         Post saving
changing post creation                                             coordinates
or update workflows                                                validation,
database updates,
metadata/terms,
cache updates, and
hooks. A change to
execution order or
omitted side
effects can break
plugins, workflows,
or stored content.

  R7             Backward-compatibility   Medium         Public APIs and extension  Themes and plugins
constraints limit                       points                     depend on
modernization                                                      established APIs
and hooks. Removing
or changing
behavior without
compatibility
planning can break
existing sites and
integrations.
R8             Insufficient focused     Medium         Query, permissions, post   Complex behavior
tests for edge cases and                save, nonce, and HTML      depends on
extension behavior                      filtering                  combinations of
user roles, object
ownership, hooks,
malformed input,
and cache state.
Gaps in regression
tests can allow
subtle bugs to pass
unnoticed.
Prioritization
High priority
1. R1 --- Authorization checks: review permission checks around
   sensitive actions and object-specific operations.
2. R2 --- Nonce misuse: ensure nonce verification is always paired
   with the required capability check.
3. R3 --- HTML handling: verify allowlists and use
   context-appropriate escaping for output.
4. R6 --- Post workflow regressions: protect save behavior with
   tests before changing the workflow.
Medium priority
5. R4 --- Extension hook side effects: document hook behavior and
   test important integrations.
6. R5 --- Query performance: profile representative slow queries
   and verify cache behavior.
7. R7 --- Backward compatibility: document public API expectations
   and use deprecation paths where appropriate.
8. R8 --- Test coverage: add focused tests for edge cases and
   extension behavior.
Recommended Mitigation Plan
- Use current_user_can() with the relevant object ID for
  object-specific authorization checks.
- Treat nonce verification as request validation, not as permission
  granting; perform a separate capability check.
- Use the narrowest appropriate HTML allowlist and escape output for
  its final context.
- Add tests around query filters, post-save hooks, user permissions,
  nonce validation, and malformed HTML.
- Profile slow database queries before optimizing query construction
  or cache behavior.
- Preserve public APIs and hook behavior unless a compatibility plan
  is in place.
- Review changes incrementally and run the relevant PHP, JavaScript,
  and integration test suites.
Limitations
This is a codebase-level risk assessment based on the reviewed WordPress
Core functions and project architecture. It is not a full security
audit, penetration test, dependency vulnerability scan, or confirmation
that the listed issues are present in a particular deployment.
Deployment configuration, installed plugins and themes, custom code, and
the exact WordPress version can materially change the actual risk.
References
- WordPress capability API:
  https://developer.wordpress.org/plugins/users/roles-and-capabilities/
- WordPress nonce security guidance:
  https://developer.wordpress.org/apis/security/nonces/
- WordPress data validation and sanitization:
  https://developer.wordpress.org/apis/security/data-validation/
- WordPress escaping guidance:
  https://developer.wordpress.org/apis/security/escaping/
- WP_Query source:
  https://github.com/WordPress/wordpress-develop/blob/trunk/src/wp-includes/class-wp-query.php
- wp_insert_post() source:
  https://github.com/WordPress/wordpress-develop/blob/trunk/src/wp-includes/post.php
- Capability mapping source:
  https://github.com/WordPress/wordpress-develop/blob/trunk/src/wp-includes/capabilities.php
- Nonce verification source:
  https://github.com/WordPress/wordpress-develop/blob/trunk/src/wp-includes/pluggable.php
- KSES source:
  https://github.com/WordPress/wordpress-develop/blob/trunk/src/wp-includes/kses.php
