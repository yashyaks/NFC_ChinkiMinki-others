'use client'

import {
  Box,
  Stack,
  HStack,
  Heading,
  Text,
  VStack,
  useColorModeValue,
  List,
  ListItem,
  ListIcon,
  Button,
} from '@chakra-ui/react'
import { FaCheckCircle } from 'react-icons/fa'



function PriceWrapper(props) {
  const { children } = props

  return (
    <Box
      mb={4}
      shadow="base"
      borderWidth="1px"
      alignSelf={{ base: 'center', lg: 'flex-start' }}
      borderColor={useColorModeValue('gray.200', 'gray.500')}
      borderRadius={'xl'}>
      {children}
    </Box>
  )
}

export default function Pricing() {
  return (
    <Box bg={'black'}py={12}>
      <VStack spacing={2} textAlign="center">
        <Heading color='white' as="h1" fontSize="4xl">
          Plans that fit your need
        </Heading>
        <Text color='white' fontSize="lg" >
          Start with 14-day free trial. No credit card needed. Cancel at anytime.
        </Text>
      </VStack>
      <Stack
        direction={{ base: 'column', md: 'row' }}
        textAlign="center"
        justify="center"
        spacing={{ base: 4, lg: 10 }}
        py={10}>
        <PriceWrapper>
          <Box bg='black' borderRadius={15}py={4} px={12}>
            <Text color='white'fontWeight="500" fontSize="2xl">
              Hobby
            </Text>
            <HStack justifyContent="center">
              <Text color='red.500'fontSize="3xl" fontWeight="600">
                $
              </Text>
              <Text color='red.500' fontSize="5xl" fontWeight="900">
                79
              </Text>
              <Text color='red.500' fontSize="3xl">
                /month
              </Text>
            </HStack>
          </Box>
          <VStack
            bg='#141429'
            
            py={4}
            borderBottomRadius={'xl'}>
            <List color={'white'} spacing={3} textAlign="start" px={12}>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                unlimited build minutes
              </ListItem>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                Lorem, ipsum dolor.
              </ListItem>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                5TB Lorem, ipsum dolor.
              </ListItem>
            </List>
            <Box w="80%" pt={7}>
              <Button 
              rounded={'full'}
              _hover={{
                transform: 'scale(1.1)',
              }} 
              w="full" 
              colorScheme="red">
                Start trial
              </Button>
            </Box>
          </VStack>
        </PriceWrapper>

        <PriceWrapper>
          <Box position="relative">
            <Box
              position="absolute"
              top="-16px"
              left="50%"
              style={{ transform: 'translate(-50%)' }}>
              <Text
                textTransform="uppercase"
                bg={useColorModeValue('red.300', 'red.700')}
                bgGradient= 'linear(to-l, #3131D8, red.500)'
                px={3}
                py={1}
                color={'white'}
                fontSize="sm"
                fontWeight="600"
                rounded="xl">
                Most Popular
              </Text>
            </Box>
            <Box py={4} px={12}>
              <Text color="white" fontWeight="500" fontSize="2xl">
                Growth
              </Text>
              <HStack justifyContent="center">
                <Text color="red.500" fontSize="3xl" fontWeight="600">
                  $
                </Text>
                <Text color="red.500" fontSize="5xl" fontWeight="900">
                  149
                </Text>
                <Text color="red.500" fontSize="3xl" >
                  /month
                </Text>
              </HStack>
            </Box>
            <VStack
                bgGradient= 'linear(to-l, #3131D8, red.500)' 
              
              py={4}
              borderBottomRadius={'xl'}>
              <List color={'white'}  spacing={3} textAlign="start" px={12}>
                <ListItem>
                  <ListIcon as={FaCheckCircle} color="green.500" />
                  unlimited build minutes
                </ListItem>
                <ListItem>
                  <ListIcon as={FaCheckCircle} color="green.500" />
                  Lorem, ipsum dolor.
                </ListItem>
                <ListItem>
                  <ListIcon as={FaCheckCircle} color="green.500" />
                  5TB Lorem, ipsum dolor.
                </ListItem>
                <ListItem>
                  <ListIcon as={FaCheckCircle} color="green.500" />
                  5TB Lorem, ipsum dolor.
                </ListItem>
                <ListItem>
                  <ListIcon as={FaCheckCircle} color="green.500" />
                  5TB Lorem, ipsum dolor.
                </ListItem>
              </List>
              <Box w="80%" pt={7}>
              <Button
              rounded={'full'} 
              _hover={{
                transform: 'scale(1.1)',
              }} 
              w="full" 
              >
                  Start trial
                </Button>
              </Box>
            </VStack>
          </Box>
        </PriceWrapper>
        <PriceWrapper>
          <Box py={4} px={12}>
            <Text color={'white'}fontWeight="500" fontSize="2xl">
              Scale
            </Text>
            <HStack justifyContent="center">
              <Text color={'red.500'} fontSize="3xl" fontWeight="600">
                $
              </Text>
              <Text color={'red.500'} fontSize="5xl" fontWeight="900">
                349
              </Text>
              <Text color={'red.500'} fontSize="3xl" >
                /month
              </Text>
            </HStack>
          </Box>
          <VStack
          bg='#141429'
            
            py={4}
            borderBottomRadius={'xl'}>
            <List color='white'spacing={3} textAlign="start" px={12}>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                unlimited build minutes
              </ListItem>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                Lorem, ipsum dolor.
              </ListItem>
              <ListItem>
                <ListIcon as={FaCheckCircle} color="green.500" />
                5TB Lorem, ipsum dolor.
              </ListItem>
            </List>
            <Box w="80%" pt={7}>
            <Button 
              _hover={{
                transform: 'scale(1.1)',
              }} 
              rounded={'full'}
              w="full" 
              colorScheme="red">
                Start trial
              </Button>
            </Box>
          </VStack>
        </PriceWrapper>
      </Stack>
    </Box>
  )
}