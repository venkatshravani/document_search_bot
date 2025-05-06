import React, { useState, useEffect } from "react";
import axios from "axios";

const SearchBox = () => {
  const [searchResults, setSearchResults] = useState([]);  // Default to an empty array
  const [loading, setLoading] = useState(true);            // Track loading state
  const [query, setQuery] = useState("");

  // Fetching search results based on query
  useEffect(() => {
    const fetchSearchResults = async () => {
      if (query.trim() === "") {
        setSearchResults([]);  // If query is empty, set empty results
        setLoading(false);
        return;
      }

      try {
        setLoading(true); // Start loading
        const response = await axios.get(`http://127.0.0.1:8000/api/search/?q=${query}`);
        setSearchResults(response.data); // Assume response.data is an array
      } catch (error) {
        console.error("Error fetching search results:", error);
        setSearchResults([]); // Handle errors gracefully
      } finally {
        setLoading(false);  // End loading
      }
    };

    fetchSearchResults();
  }, [query]); // Only run when query changes

  const handleChange = (event) => {
    setQuery(event.target.value);  // Update query on input change
  };

  return (
    <div>
      <h2>Search Documents</h2>
      <input
        type="text"
        value={query}
        onChange={handleChange}
        placeholder="Search..."
      />
      <div>
        {loading ? (
          <p>Loading...</p>
        ) : (
          // Safely handle the map() call with an array check
          Array.isArray(searchResults) && searchResults.length > 0 ? (
            searchResults.map((item, index) => (
              <div key={index}>
                <h4>{item.title}</h4>
                <p>{item.description}</p>
              </div>
            ))
          ) : (
            <p>No results found</p>
          )
        )}
      </div>
    </div>
  );
};

export default SearchBox;


