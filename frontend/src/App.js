import './App.css';

import { ChakraProvider } from '@chakra-ui/react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Hero from './components/Hero';
import Speech2text from './components/Speech2text';

function App() {
  return (
    <ChakraProvider>
    <Router>
      <Routes>
        <Route path='/' element={<Hero/>} />
        <Route path='/Speech2text' element={<Speech2text/>}/>
      </Routes>
    </Router>
    </ChakraProvider>
  );
}

export default App;

