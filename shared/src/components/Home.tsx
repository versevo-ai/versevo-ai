import Image from "next/image"
import { Button, Container } from "../index"

export function Home() {
    return (
        <Container>
            <header className="py-4">
                <span className="flex -space-x-2 items-center">
                    <Image src={'/images/Logo.png'} alt="Logo" width={70} height={70} />
                    <h1 className="text-3xl font-semibold">ersevo</h1>
                </span>
            </header>
            <div className="relative mt-24 flex justify-between items-start">
                <div className="space-y-8">
                    <div className="text-6xl font-bold">
                        <h1>Harness Real-time</h1>
                        <h1>Market Intelligence</h1>
                        <h1>with Versevo</h1>
                    </div>
                    <div className="flex flex-wrap w-96">
                        <p className="text-2xl ">Utilize AI-driven insights to stay ahead in the dynamic world of finance.</p>
                    </div>
                    <Button className="w-56 rounded-full py-7 bg-[#0059FF] hover:bg-[#0038a1] text-md">Explore</Button>
                </div>
                {/* <video width="60%" height="240" autoPlay loop>
                    <source className="bg-transparent" src="/Videos/wave.gif" type="video/mp4" />
                    Your browser does not support the video tag.
                </video> */}
                <Image className="absolute right-0 -top-10" src={'/images/wave.gif'} alt="wave" width={800} height={500}/>
            </div>
        </Container>
    )
}