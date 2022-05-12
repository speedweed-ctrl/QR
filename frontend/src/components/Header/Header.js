import React , {useState} from 'react'

const Header = () => {
    const [navBarOpen , setNavBarOpen]=useState(false)
  return (
    <nav class="flex items-center justify-between flex-wrap bg-cl p-6">
        <div class="flex items-center flex-shrink-0 text-white mr-6">
            <span class="text-4xl  text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500  ">lorem ipsum</span>
        </div>
        <div class="block lg:hidden">
            <button class="flex items-center px-3 py-2 border rounded text-ha border-ha hover:text-white hover:border-white"onClick={()=>setNavBarOpen(!navBarOpen)}>
            <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
            </button>
        </div>
        <div class={navBarOpen? "w-full block flex-grow lg:flex lg:items-center lg:w-auto":"w-full block flex-grow lg:flex lg:items-center lg:w-auto hidden"}>
            <div class="text-sm lg:flex-grow">
                <a href="#responsive-header" class="text-xl block mt-4 lg:inline-block lg:mt-0 text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500  4">
                    somthing
                </a>
                <a href="#responsive-header" class="text-xl block mt-4 lg:inline-block lg:mt-0 text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500  ">
                    somthing
                </a>
                <a href="#responsive-header" class="text-xl block mt-4 lg:inline-block lg:mt-0 text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500  ">
                    somthing
                </a>
            </div>
                
        </div>
</nav>
  )
}

export default Header