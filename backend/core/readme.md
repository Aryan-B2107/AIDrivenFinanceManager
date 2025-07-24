This module does the foundational work required to run and connect the other backend apps.

Development Roadmap:

-Set up the custom Django user model (if needed), using email instead of username for auth.
-Add global middleware (e.g., request logging, user tracking, or CORS).
-Create utility functions (like date parsing, goal validation, budget calculators) in a utils folder.
-Write project-wide constants, enums, or config files (e.g., default spending categories).
-Optionally add signal handlers (e.g., send welcome email on user creation).
-Handle authentication and permissions setup if needed centrally.