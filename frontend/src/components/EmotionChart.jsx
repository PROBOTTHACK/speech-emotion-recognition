import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
  CartesianGrid,
} from "recharts";

import { motion } from "framer-motion";

const COLORS = [
  "#22D3EE",
  "#8B5CF6",
  "#F43F5E",
  "#FACC15",
  "#34D399",
  "#FB7185",
  "#60A5FA",
];

const EmotionChart = ({ probabilities }) => {

  const data = Object.entries(probabilities).map(
    ([emotion, value]) => ({
      emotion,
      confidence: value,
    })
  );

  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="mt-10 backdrop-blur-xl bg-white/5 border border-white/10 rounded-3xl p-8 shadow-[0_0_40px_rgba(34,211,238,0.08)]"
    >

      {/* TITLE */}
      <div className="mb-8">
        <h2 className="text-3xl font-bold bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent">
          Emotion Analytics
        </h2>

        <p className="text-gray-400 mt-2">
          AI confidence distribution across emotions
        </p>
      </div>

      {/* CHART */}
      <div className="w-full h-[350px]">

        <ResponsiveContainer width="100%" height="100%">

          <BarChart
            data={data}
            margin={{
              top: 20,
              right: 10,
              left: -20,
              bottom: 5,
            }}
          >

            {/* GRID */}
            <CartesianGrid
              strokeDasharray="3 3"
              stroke="rgba(255,255,255,0.05)"
              vertical={false}
            />

            {/* X AXIS */}
            <XAxis
              dataKey="emotion"
              tick={{
                fill: "#9CA3AF",
                fontSize: 14,
              }}
              axisLine={false}
              tickLine={false}
            />

            {/* Y AXIS */}
            <YAxis
              tick={{
                fill: "#9CA3AF",
                fontSize: 13,
              }}
              axisLine={false}
              tickLine={false}
            />

            {/* TOOLTIP */}
            <Tooltip
                cursor={{
                    fill: "rgba(255,255,255,0.03)",
                }}
                contentStyle={{
                    background: "rgba(15,23,42,0.95)",
                    border: "1px solid rgba(255,255,255,0.08)",
                    borderRadius: "16px",
                    color: "#FFFFFF",
                    backdropFilter: "blur(12px)",
                }}
                labelStyle={{
                    color: "#22D3EE",
                    fontWeight: "600",
                }}
                itemStyle={{
                    color: "#FFFFFF",
                }}
            />

            {/* BAR */}
            <Bar
              dataKey="confidence"
              radius={[12, 12, 0, 0]}
              barSize={42}
            >

              {data.map((entry, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index % COLORS.length]}
                />
              ))}

            </Bar>

          </BarChart>

        </ResponsiveContainer>

      </div>
    </motion.div>
  );
};

export default EmotionChart;