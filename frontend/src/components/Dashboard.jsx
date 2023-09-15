import React from 'react'
import { Grid, GridItem, useMediaQuery, Box } from '@chakra-ui/react'
import Controls from './Controls'

export default function Dashboard() {
  const [isSmallerThan1200] = useMediaQuery("(max-width: 1200px)");

  return (
    <>
    <Grid
      templateAreas={
        isSmallerThan1200
          ? `"video"
             "output"
             "controls"`
          : `"video output"
             "video controls"`
      }
      gridTemplateRows={
        isSmallerThan1200
          ? '500px 500px 500px'
          : '450px 450px'
      }
      gridTemplateColumns={
        isSmallerThan1200
          ? '375px'
          : '1300px 600px'
      }
      h='920px'
      gap='1'
      fontWeight='bold'

    >
      <GridItem
        borderRadius='20'
        m='2'
        p='2'
        bg='pink.300'
        area={'video'}
      >
        video
      </GridItem>

      <GridItem
        borderRadius='20'
        m='2'
        p='2'
        bg='gray.300'
        area={'output'}
      >
        output
      </GridItem>

      <GridItem
        bg='red.100'
        border='2px'
        borderColor='red.500'
        borderRadius='20'
        m='2'
        p='2'
        area={'controls'}
      >
        <Controls />
      </GridItem>
    </Grid>
    </>
  )
}
