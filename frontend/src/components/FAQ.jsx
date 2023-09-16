'use client'

import {
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  Flex,
  useColorModeValue,
  Text,
  Container,
} from '@chakra-ui/react'

import { ChevronDownIcon } from '@chakra-ui/icons'

export default function FAQ() {
  return (
    <Flex
      minH={'100vh'}
      align={'center'}
      justify={'center'}
      bg={'black'}>
      <Container>
        <Text fontSize={{ base: '2xl', sm: '4xl' }} fontWeight={'bold'} color={'red.500'}>
            FAQ
        </Text>
        <Accordion allowMultiple width="100%" maxW="lg" rounded="lg">
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text color='red.500' fontSize="md">What is Chakra UI?</Text>
              <ChevronDownIcon fontSize="24px" color='red.500' />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="white">
                Chakra UI is a simple and modular component library that gives developers
                the building blocks they need to create web applications.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md" color='red.500' >What advantages to use?</Text>
              <ChevronDownIcon fontSize="24px" color='red.500'/>
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color='white'>
                Chakra UI offers a variety of advantages including ease of use,
                accessibility, and customization options. It also provides a comprehensive
                set of UI components and is fully compatible with React.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}>
              <Text fontSize="md" color='red.500'>How to start using Chakra UI?</Text>
              <ChevronDownIcon color='red.500' fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color='white'>
                To get started with Chakra UI, you can install it via npm or yarn, and
                then import the components you need in your project. The Chakra UI
                documentation is also a great resource for getting started and learning
                more about the library.
              </Text>
            </AccordionPanel>
          </AccordionItem>
        </Accordion>
      </Container>
    </Flex>
  )
}