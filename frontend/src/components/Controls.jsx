import React, { useState }  from 'react'
import { Select, Text, Box, Stack, HStack, Button} from '@chakra-ui/react'
import { Switch } from '@chakra-ui/react'
import {
    Slider,
    SliderTrack,
    SliderFilledTrack,
    SliderThumb,
  } from '@chakra-ui/react'

import { FcSpeaker } from 'react-icons/fc';
import { BsFillMicFill, BsFillMicMuteFill } from 'react-icons/bs';

import { Radio, RadioGroup } from '@chakra-ui/react'

export default function Controls() {
    const [isMicMuted, setIsMicMuted] = useState(false);

    const toggleMic = () => {
      setIsMicMuted((prevIsMicMuted) => !prevIsMicMuted);
    };

  return (
    <div>
        <Text pb='2' fontSize={24}> CONTROLS </Text>
        <Text fontSize={20}> ASL to Text Conversion </Text>
        <Select placeholder='Select a Language' size='lg'  variant='outline' borderColor='red.500' color='black'> 
            <option value='option1'>English</option>
            <option value='option2'>Hindi</option>
            <option value='option3'>Marathi</option>
        </Select>

        <Text fontSize={20} pt={2}>
            Text to Speech
            <Switch pl='5'colorScheme='red' size='lg' /> 
        </Text>
        <Text fontSize={18} pt={1}> Volume </Text>
        <HStack>
            <Box>
                <FcSpeaker size={24}/>
            </Box>
                <Slider aria-label='slider-ex-4' defaultValue={30}>
                    <SliderTrack bg='gray.100'>
                        <SliderFilledTrack bg='red' />
                    </SliderTrack >
                    <SliderThumb boxSize={4}/>
                </Slider>
        </HStack>
        <HStack>
            <Text>Voice Gender</Text>
            <RadioGroup defaultValue='2'>
            <Stack spacing={5} direction='row'>
                <Radio colorScheme='red' value='male'>
                    Male
                </Radio>
                <Radio colorScheme='red' value='female'>
                    Female
                </Radio>
            </Stack>
            </RadioGroup>
        </HStack>

        <Text fontSize={20}> Speech to Text </Text>
        <HStack>
        <Select placeholder='Select a Language' size='lg'  variant='outline' borderColor='red.500' color='black'> 
            <option value='option1'>English</option>
            <option value='option2'>Hindi</option>
            <option value='option3'>Marathi</option>
        </Select>
        <Button colorScheme='red' variant='ghost' onClick={toggleMic}>
        {isMicMuted ? (
            <div>
            <div>
                Microphone
            </div>
            <BsFillMicMuteFill size={28} />
            </div>
        ) : (
            <div>
            <div>
                Microphone
            </div>
            <BsFillMicFill size={28} />
            </div>
        )}
        </Button>

        </HStack>
    </div>
  )
}
