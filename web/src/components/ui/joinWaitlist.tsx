export default function JoinWaitlist() {
    return (
        <div className="w-full flex justify-center px-4 py-4">
            <form className="flex w-full max-w-2xl rounded-full overflow-hidden shadow-md bg-[#DFF6FD]">
                <input
                    type="email"
                    placeholder="Enter your Email Address"
                    className="flex-1 px-2 py-2 text-lg text-[#075985] bg-[#DFF6FD] focus:outline-none rounded-full"
                    required
                />
                
                <div className="p-[2px] rounded-full bg-[conic-gradient(at_center,_#0D72DF,_#073E79,_#88E4FF,_#073E79)]">
                    <button
                        type="submit"
                        className="text-lg px-2 py-2 font-semibold text-[#075985] bg-[#B2E2F0] rounded-full hover:bg-[#cbe9f6] transition-colors w-full h-full"
                    >
                        Join Waitlist
                    </button>
                </div>
            </form>
        </div>
    );
}
