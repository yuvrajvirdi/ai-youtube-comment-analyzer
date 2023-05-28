import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { IComment } from '@/interfaces/comment';
import 'tailwindcss/tailwind.css';

// Helper function to extract videoId from Youtube URL
function getVideoId(url: string) {
  let videoId = url.split('v=')[1];
  const ampersandPosition = videoId.indexOf('&');
  if (ampersandPosition !== -1) {
    videoId = videoId.substring(0, ampersandPosition);
  }
  return videoId;
}



export default function Index(): JSX.Element {
  const [videoUrl, setVideoUrl] = useState('');
  const [videoAnalysis, setVideoAnalysis] = useState<IComment[]>([]);

  // url handling
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setVideoUrl(e.target.value);
  };

  // form submit handling
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const videoId = getVideoId(videoUrl);

    axios.get(`http://127.0.0.1:5000/analyze?id=${videoId}&maxResults=50`)
    .then(response => {
      setVideoAnalysis(response.data);
    })
    .catch(error => {
      console.error('There was an error!', error);
    });

    setVideoUrl('');
  };
  
  return (

    <>
      <link rel="stylesheet" href="https://rsms.me/inter/inter.css" />
      <script src="https://cdn.jsdelivr.net/gh/alpinejs/alpine@v2.x.x/dist/alpine.min.js" defer></script>
      <main className="font-sans">
        <div className="mt-5 text-3xl font-medium text-center">Youtube Spam Detector</div>
        <div className="max-w-2xl mx-auto">

        <form className="mt-4" onSubmit={handleSubmit}>   
          <label htmlFor="default-search" className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300">Search</label>
          <div className="relative">
              <div className="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
                  <svg className="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
              </div>
              <input type="search" id="default-search" className="block p-4 pl-10 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Paste your youtube video URL here..." required onChange={handleInputChange} value={videoUrl}/>
              <button type="submit" className="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</button>
          </div>
        </form>

        <div className="grid grid-cols-2 gap-4"> {/* here we defined a grid with 2 columns and gap of 4 */}
          {videoAnalysis.map((analysis: IComment) => (
          <div className="mt-4 p-4 border rounded">
              <p><strong>Author:</strong> {analysis.author}</p>
              <p><strong>Comment:</strong> {analysis.comment}</p>
              <p><strong>Is Spam:</strong> {analysis.isSpam ? 'Yes' : 'No'}</p>
              <p><strong>Like Count:</strong> {analysis.likeCount}</p>
              <p><strong>Published Date:</strong> {analysis.publishedDate}</p>
              <p><strong>Sentiment:</strong> {analysis.sentiment}</p>
              <p><strong>Topics:</strong> {analysis.topics ? analysis.topics.join(', ') : ''}</p>
              <p><strong>Type:</strong> {analysis.type}</p>
          </div>
          ))}
        </div>

      </div>
      </main>
    </>
  );
}
