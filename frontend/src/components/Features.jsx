import React from 'react'
import {
    Box,
    Container,
    Heading,
    SimpleGrid,
    Icon,
    Text,
    Stack,
    HStack,
    VStack,
  } from '@chakra-ui/react';
  import { CheckIcon } from '@chakra-ui/icons';

  const features = Array.apply(null, Array(8)).map(function (x, i) {
    return {
      id: i,
      title: 'Lorem ipsum dolor sit amet',
      text: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam.',
    };
  });
  
  
export default function Features() {
  return (
    <Box p={4}bg={'black'}>
    <Stack spacing={4} as={Container} maxW={'3xl'} textAlign={'center'}>
      <Heading fontSize={{ base: '2xl', sm: '4xl' }} bgGradient= 'linear(to-l, #3131D8, red.500)'  bgClip='text'>Unlocking Your Potential!</Heading>
      <Text color={'white'} fontSize={'xl'}>
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua.
      </Text>
    </Stack>

    <Container maxW={'6xl'} mt={10}>
      <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} spacing={10}>
        {features.map((feature) => (
          <HStack key={feature.id} align={'top'}>
            <Box color={'#dd4d51'} px={2}>
              <Icon as={CheckIcon} />
            </Box>
            <VStack align={'start'}>
              <Text fontWeight={600} color={'white'}>{feature.title}</Text>
              <Text color={'gray.600'}>{feature.text}</Text>
            </VStack>
          </HStack>
        ))}
      </SimpleGrid>
    </Container>
  </Box>
);
}
