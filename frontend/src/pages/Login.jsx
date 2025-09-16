function Login() {
  return (
    <div className="max-w-md mx-auto bg-white shadow-lg rounded-xl p-6">
      <h2 className="text-2xl font-bold mb-4 text-indigo-600">Login</h2>
      <form className="space-y-4">
        <input
          type="email"
          placeholder="Email"
          className="w-full border px-3 py-2 rounded-md"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full border px-3 py-2 rounded-md"
        />
        <button
          type="submit"
          className="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700"
        >
          Log In
        </button>
      </form>
    </div>
  );
}
export default Login;
