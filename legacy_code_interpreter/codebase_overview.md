Codebase Overview --- WordPress Core
Project: WordPress Core
Repository: WordPress/wordpress-develop
Analysis date: November 16, 2026
1. Project Age
WordPress was first publicly released as version 0.7 on May 27,
2003. It began as a fork of the b2/cafelog project, created by Matt
Mullenweg and Mike Little.

As of November 16, 2026, WordPress has been publicly maintained for
approximately 23 years and 5 months.
2. Codebase Size (LOC)
A third-party code-count report for the WordPress repository dated
October 26, 2026 reports approximately:
- 4,014 files
- 1,242,204 total lines (including comments and blank lines)
- 795,626 code lines
The reported code-language distribution is approximately: - PHP: 47.8% -
CSS: 21.2% - JavaScript: 18.3%

These figures are an estimate from an external code-counting service.
Counts can differ depending on the repository snapshot,
generated/minified assets, bundled libraries, and counting rules.
3. Main Technologies and Dependencies
Core technologies
- PHP --- primary server-side programming language.
- MySQL or MariaDB --- relational database layer.
- JavaScript --- browser-side functionality and the block editor.
- HTML and CSS --- page structure and styling.
Development and build dependencies
The current development repository also uses Node.js and npm for
JavaScript tooling and asset builds.

The repository's composer.json declares PHP >=7.4 and requires the
PHP hash and json extensions. It also lists optional PHP extensions,
including mysqli, curl, mbstring, openssl, xml-related
extensions, and others.

The development package.json includes front-end libraries and tooling
such as React, jQuery, Lodash, Grunt, Webpack, Sass, and Playwright.
These are development/build dependencies and should not all be confused
with mandatory runtime requirements for every WordPress installation.
4. Known Maintenance Challenges and Potential Pain Points
The following are maintenance risks and complexity areas to investigate
in a mature, long-running codebase. They are not claims that every item
is currently an unresolved defect.
- Backward compatibility: WordPress supports a large ecosystem of
  themes and plugins. Changes to established APIs can break existing
  integrations, so core changes require careful compatibility review.
- Large and distributed codebase: The official Core Codebase
  Handbook describes around 1,000 files and directories in the core
  source layout, organized mainly under areas such as wp-admin and
  wp-includes. Finding the correct implementation path can take time
  for new contributors.
- Legacy and deprecated APIs: The codebase retains deprecated
  functions and compatibility paths. Contributors need to understand
  which APIs are current and which are retained for older
  integrations.
- Third-party and bundled components: Core includes or integrates
  external libraries. Their versions, update process, and interactions
  add maintenance work.
- Broad test and build workflow: The development repository uses
  multiple tools for PHP tests, JavaScript tests, end-to-end tests,
  linting, and asset builds. New contributors must learn the relevant
  workflow before making safe changes.
- Security-sensitive surface area: Authentication, permissions,
  input validation, database access, file uploads, and plugin/theme
  integration require careful review because WordPress is extensible
  and widely deployed.
5. Summary
WordPress Core is a mature open-source content management system with
more than 23 years of public development history. It is primarily built
with PHP and uses a relational database, JavaScript, HTML, and CSS. Its
size, compatibility requirements, historical APIs, external components,
and broad testing workflow make it a useful case study for legacy-code
analysis and modernization planning.
6. Sources
1. WordPress --- About and project history:
   https://wordpress.org/about/
2. WordPress --- First public release announcement (May 27, 2003):
   https://wordpress.org/news/2003/05/WordPress-now-available/
3. WordPress Core Codebase Handbook:
   https://make.wordpress.org/core/handbook/contribute/codebase/
4. WordPress development repository:
   https://github.com/WordPress/wordpress-develop
5. composer.json in the development repository:
   https://github.com/WordPress/wordpress-develop/blob/trunk/composer.json
6. package.json in the development repository:
   https://github.com/WordPress/wordpress-develop/blob/trunk/package.json
7. External code-count report (snapshot dated October 26, 2026):
   https://octocounts.com/compare/wordpress-vs-drupal
Note: The LOC figures are repository-wide estimates from the cited
third-party report, not an official WordPress-maintained metric. The
maintenance challenges are framed as areas for investigation based on
the project's architecture and ecosystem.
