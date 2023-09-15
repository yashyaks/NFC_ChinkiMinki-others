import Webcam from 'react-webcam';

const CustomWebcam = () => {
  const [screenshots, setScreenshots] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      const screenshot = webcam.getScreenshot();
      setScreenshots([...screenshots, screenshot]);
    }, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <Webcam ref={webcam} />
  );
};

export default CustomWebcam;
