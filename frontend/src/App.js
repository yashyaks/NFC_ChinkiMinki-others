import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Dashboard from './components/Dashboard'
function App() {
  return (
    <ChakraProvider>
    <Router>
      <Routes>
        {/*<Route path='/' element={<Hero/>} />*/}
        <Route path='/' element={<Dashboard/>} />
      </Routes>
    </Router>
    </ChakraProvider>
  );
}

export default App;
