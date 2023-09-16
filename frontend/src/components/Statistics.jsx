'use client'

import {
  Box,
  chakra,
  Flex,
  SimpleGrid,
  Stat,
  StatLabel,
  StatNumber,
  useColorModeValue,
} from '@chakra-ui/react'

import { BsPerson } from 'react-icons/bs'
import { FiServer } from 'react-icons/fi'
import { GoLocation } from 'react-icons/go'



function StatsCard(props) {
  const { title, stat, icon } = props
  return (
    <Stat
      px={{ base: 2, md: 4 }}
      py={'5'}
      shadow={'xl'}
      
      border={'1px solid'}
      borderColor={useColorModeValue('white')}
      rounded={'lg'}
      >
      <Flex justifyContent={'space-between'}>
        <Box pl={{ base: 2, md: 4 }}>
          <StatLabel bgGradient= 'linear(to-l, #3131D8, red.500)' bgClip= 'text' fontWeight={'medium'} isTruncated>
            {title}
          </StatLabel>
          <StatNumber bgGradient= 'linear(to-l, #3131D8, red.500)' bgClip= 'text' fontSize={'2xl'} fontWeight={'medium'}>
            {stat}
          </StatNumber>
        </Box>
        <Box
          my={'auto'}
          color={useColorModeValue('white')}
          alignContent={'center'}>
          {icon}
        </Box>
      </Flex>
    </Stat>
  )
}

export default function Statistics() {
  return (
    <Box bg={'black'}>


    <Box  maxW="7xl" mx={'auto'} pt={5} pb={100} pl={100} pr={100} px={{ base: 20, sm: 80, md: 110 }} >
      <chakra.h1 color={"white"} textAlign={'center'} fontSize={'4xl'} py={10} fontWeight={'bold'}>
        Our company is expanding, you could be too.
      </chakra.h1>
      <SimpleGrid  columns={{ base: 1, md: 3 }} spacing={{ base: 5, lg: 8 }}>
        <StatsCard title={'Users'} stat={'5,000'} icon={<BsPerson size={'3em'} />} />
        <StatsCard title={'Servers'} stat={'1,000'} icon={<FiServer size={'3em'} />} />
        <StatsCard title={'Datacenters'} stat={'7'} icon={<GoLocation size={'3em'} />} />
      </SimpleGrid>
    </Box>
    </Box>
  )
}