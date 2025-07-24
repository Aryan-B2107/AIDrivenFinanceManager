What this module does is handle all API requests between the frontend and your Django REST backend.

Development Roadmap:

Create a api.js or axiosClient.js to configure base URL and headers.
Write service functions like getExpenses(), postGoal(), getLeaderboard(), chatWithAI().
Handle auth tokens (JWT/localStorage/secure storage) for protected routes.
Add error handling and response formatting logic.
Group services by domain: financeService.js, aiService.js, scoreService.js, etc.