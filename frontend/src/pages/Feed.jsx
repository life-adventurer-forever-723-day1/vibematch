function Feed() {
  return (
    <div className="max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold text-indigo-600 mb-4">Community Feed</h2>
      <div className="bg-white shadow-md rounded-lg p-4 mb-3">
        <p className="text-gray-700">💬 “What’s your go-to comfort food?”</p>
        <div className="flex space-x-4 mt-2">
          <button className="text-indigo-600 hover:underline">Like</button>
          <button className="text-indigo-600 hover:underline">Comment</button>
          <button className="text-indigo-600 hover:underline">Poke</button>
        </div>
      </div>
    </div>
  );
}
export default Feed;
