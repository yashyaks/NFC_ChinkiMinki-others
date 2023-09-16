import './App.css';

import { ChakraProvider } from '@chakra-ui/react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Hero from './components/Hero';

function App() {
  return (
    <ChakraProvider>
    <Router>
      <Routes>
        <Route path='/' element={<Hero/>} />
      </Routes>
    </Router>
    </ChakraProvider>
  );
}

export default App;

