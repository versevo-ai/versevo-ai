export default function JoinWaitlist() {
    return (
        <div className="w-full max-w-[600px] mx-auto px-4 sm:px-0">
            <form className="flex flex-col sm:flex-row w-full gap-3 sm:gap-0 sm:rounded-[40px] overflow-hidden shadow-md bg-transparent">
                <input
                    type="email"
                    placeholder="Enter your Email Address"
                    className="w-full px-4 sm:px-6 py-3 text-base sm:text-xl text-blue-900 bg-blue-100 focus:outline-none rounded-[40px] sm:rounded-l-[40px] sm:rounded-tr-none sm:rounded-br-none"
                    required
                />
                <button
                    type="submit"
                    className="w-full sm:w-[198px] py-3 text-base sm:text-xl text-blue-900 bg-green-300 hover:bg-green-400 transition-colors rounded-[40px] sm:rounded-r-[40px] sm:rounded-tl-none sm:rounded-bl-none"
                >
                    Join Waitlist
                </button>
            </form>
        </div>
    );
}
