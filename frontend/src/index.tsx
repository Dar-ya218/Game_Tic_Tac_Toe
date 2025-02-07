import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import 'antd/dist/reset.css';  // Importar estilos de Ant Design
import './styles/global.css';  // Importar estilos globales

// Renderizar la aplicación en el DOM
const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
