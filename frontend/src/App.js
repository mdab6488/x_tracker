import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { formatDistance } from 'date-fns';
import './App.css';

function App() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPosts = async () => {
      const apiUrl = process.env.REACT_APP_API_URL
        ? `${process.env.REACT_APP_API_URL}/api/posts/latest/`
        : "http://localhost:8000/api/posts/latest/";
  
      console.log("Fetching from:", apiUrl); // Debugging Log
  
      try {
        const response = await axios.get(apiUrl);
        setPosts(Array.isArray(response.data) ? response.data : []);
        setLoading(false);
      } catch (err) {
        setError("Failed to fetch posts");
        setLoading(false);
        console.error("Error fetching posts:", err.message);
      }
    };
  
    fetchPosts();
    const interval = setInterval(fetchPosts, 30000);
    return () => clearInterval(interval);
  }, []);  

  if (loading) return <div className="flex items-center justify-center min-h-screen">Loading...</div>;
  if (error) return <div className="text-red-500 text-center p-4">{error}</div>;

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4">
          <h1 className="text-3xl font-bold text-gray-900">Latest X Posts</h1>
        </div>
      </header>
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="divide-y divide-gray-200">
            {Array.isArray(posts) && posts.map((post) => (
              <div key={post.id} className="py-4">
                <div className="flex space-x-3">
                  <div className="flex-1 space-y-1">
                    <div className="flex items-center justify-between">
                      <h3 className="text-sm font-medium">{post.account.display_name}</h3>
                      <p className="text-sm text-gray-500">
                        {formatDistance(new Date(post.posted_at), new Date(), { addSuffix: true })}
                      </p>
                    </div>
                    <p className="text-sm text-gray-800">{post.content}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;