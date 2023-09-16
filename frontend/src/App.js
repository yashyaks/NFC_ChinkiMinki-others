import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import Dashboard from './components/Dashboard'
import Hero from './components/Hero'

function App() {
  return (
    <ChakraProvider>
    <Router>
      <Routes>
        <Route path='/' element={<Hero/>} />
        <Route path='/dashboard' element={<Dashboard/>} />
      </Routes>
    </Router>
    </ChakraProvider>
  );
}

export default App;
