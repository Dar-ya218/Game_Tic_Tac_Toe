import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ConfigProvider } from 'antd';
import HomePage from './pages/HomePage';
import GamePage from './pages/GamePage';
import SummaryPage from './pages/SummaryPage';

const App: React.FC = () => {
    return (
        <ConfigProvider>
            <Router>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/game/:gameId" element={<GamePage />} />
                    <Route path="/summary" element={<SummaryPage />} />
                </Routes>
            </Router>
        </ConfigProvider>
    );
};

export default App;
