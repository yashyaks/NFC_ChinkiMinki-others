import React, { useRef, useEffect } from 'react';
import Webcam from 'react-webcam';

export default function CustomWebcam() {
  const webRef = useRef(null);
  const webcamStyles = {
    borderRadius: '15px',
  };
  const videoConstraints = {
    width: 1280,
    height: 720,
  };

  const captureScreenshot = () => {
    const screenshot = webRef.current.getScreenshot();
    // Do something with the screenshot, e.g., save it or display it.
    console.log('Captured screenshot:', screenshot);
  };

  useEffect(() => {
    // Set up a timer to capture a screenshot every 500ms
    const screenshotInterval = setInterval(captureScreenshot, 500);

    // Clean up the timer when the component unmounts
    return () => clearInterval(screenshotInterval);
  }, []);

  return (
    <div>
      <Webcam
        mirrored={true}
        style={webcamStyles}
        videoConstraints={videoConstraints}
        ref={webRef}
      />
    </div>
  );
}
