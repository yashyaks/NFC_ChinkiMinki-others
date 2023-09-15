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
        <Text p='2' fontSize={24}> CONTROLS </Text>
        <Text p='2' fontSize={20}> ASL to Text Conversion </Text>
        <Select p='2' placeholder='Select a Language' size='lg'  variant='outline' borderColor='red.500' color='black'> 
            <option value='option1'>English</option>
            <option value='option2'>Hindi</option>
            <option value='option3'>Marathi</option>
        </Select>

        <Text fontSize={20} p={2}>
            Text to Speech
            <Switch  pl='5'colorScheme='red' size='lg' /> 
        </Text>
        <Text pl ='2' pr ='2' fontSize={18}> Volume </Text>
        <HStack pl='2' pr ='2'>
            <Box pl='2' pr='2'>
                <FcSpeaker size={24}/>
            </Box>
                <Slider aria-label='slider-ex-4' defaultValue={30}>
                    <SliderTrack bg='gray.100'>
                        <SliderFilledTrack bg='red' />
                    </SliderTrack >
                    <SliderThumb boxSize={4}/>
                </Slider>
        </HStack>
        <HStack p='2'>
            <Text p='2'>Voice Gender</Text>
            <RadioGroup p='2' defaultValue='2'>
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

        <Text fontSize={20} pl='2' pr='2'> Speech to Text </Text>
        <HStack pl='2' pr='2'>
        <Button pl='2' pr='2' colorScheme='red' variant='link' onClick={toggleMic}>
        {isMicMuted ? (
            <div>
            <div>
                Mic
            </div>
            <BsFillMicMuteFill size={28} />
            </div>
        ) : (
            <div>
            <div>
                Mic
            </div>
            <BsFillMicFill size={28} />
            </div>
        )}
        </Button>
        <Select p='2' placeholder='Select a Language' size='lg'  variant='outline' borderColor='red.500' color='black'> 
            <option value='option1'>English</option>
            <option value='option2'>Hindi</option>
            <option value='option3'>Marathi</option>
        </Select>
        </HStack>
    </div>
  )
}

