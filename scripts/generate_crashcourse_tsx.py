# -*- coding: utf-8 -*-
"""
Generates the complete, broadcast-quality CrashCourse10Min.tsx for Remotion.
Durations and Act offsets calibrated with crashcourse_10min_words.json.
"""

import os

TSX_PATH = "simulation/openmontage_repo/remotion-composer/src/CrashCourse10Min.tsx"

CONTENT = '''import React from "react";
import {
  AbsoluteFill,
  Audio,
  Loop,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { CaptionOverlay } from "./components/CaptionOverlay";
import wordTimestamps from "../public/assets/crashcourse_10min_words.json";

// ===========================================================================
// SHARED VISUAL HELPERS & CRASH COURSE STYLE ATOMS
// ===========================================================================

const GridBackground: React.FC<{ accentColor?: string }> = ({ accentColor = "rgba(59, 130, 246, 0.05)" }) => (
  <div
    style={{
      position: "absolute",
      inset: 0,
      backgroundImage: `linear-gradient(to right, ${accentColor} 1px, transparent 1px), linear-gradient(to bottom, ${accentColor} 1px, transparent 1px)`,
      backgroundSize: "48px 48px",
      pointerEvents: "none",
    }}
  />
);

const ActBadge: React.FC<{ actNum: number; title: string; color?: string }> = ({ actNum, title, color = "#F59E0B" }) => (
  <div
    style={{
      position: "absolute",
      top: 48,
      left: 64,
      display: "flex",
      alignItems: "center",
      gap: 12,
      backgroundColor: "rgba(15, 23, 42, 0.85)",
      border: `1px solid ${color}40`,
      borderRadius: 9999,
      padding: "10px 24px",
      boxShadow: "0 8px 24px rgba(0,0,0,0.4)",
      zIndex: 20,
    }}
  >
    <div
      style={{
        backgroundColor: color,
        color: "#0F172A",
        fontSize: 14,
        fontWeight: 900,
        fontFamily: "Space Grotesk, sans-serif",
        padding: "4px 10px",
        borderRadius: 9999,
        letterSpacing: "0.08em",
      }}
    >
      ACT {actNum}
    </div>
    <div
      style={{
        color: "#E2E8F0",
        fontSize: 16,
        fontWeight: 700,
        fontFamily: "Space Grotesk, sans-serif",
        letterSpacing: "0.05em",
        textTransform: "uppercase",
      }}
    >
      {title}
    </div>
  </div>
);

// ===========================================================================
// ACT 1: THE HOOK & THE GREAT ILLUSION (Frames 0 - 2406 / 0s - 80.2s)
// ===========================================================================
const Act1TheHook: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 650: 8 Billion humans & Earth spinning
  // 650 - 1350: 195 Flags & 12,000 Nukes vs 0 Police
  // 1350 - 1850: Domestic Court vs Superpower Dispute
  // 1850 - 2406: Title Stinger & "The Anarchy Problem"

  const countProg = spring({ frame: frame - 15, fps, config: { damping: 14, stiffness: 60 } });
  const humanCount = (interpolate(countProg, [0, 1], [1, 8.1])).toFixed(1);

  const card1Spring = spring({ frame: frame - 670, fps, config: { damping: 12, stiffness: 100 } });
  const card2Spring = spring({ frame: frame - 720, fps, config: { damping: 12, stiffness: 100 } });
  const zeroPoliceStamp = spring({ frame: frame - 820, fps, config: { damping: 10, stiffness: 180 } });

  const courtSpring = spring({ frame: frame - 1370, fps, config: { damping: 12, stiffness: 120 } });
  const stingerSpring = spring({ frame: frame - 1870, fps, config: { damping: 11, stiffness: 90 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0F172A", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(245, 158, 11, 0.06)" />
      <ActBadge actNum={1} title="The Hook & The Great Illusion" color="#F59E0B" />

      {/* Part A: 8 Billion Humans (0 - 650) */}
      {frame < 650 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div style={{ transform: `scale(${interpolate(countProg, [0, 1], [0.8, 1])})`, textAlign: "center" }}>
            <div
              style={{
                fontSize: 26,
                fontWeight: 700,
                color: "#F59E0B",
                fontFamily: "Space Grotesk, sans-serif",
                letterSpacing: "0.2em",
                textTransform: "uppercase",
                marginBottom: 16,
              }}
            >
              CRASH COURSE INTERNATIONAL RELATIONS #1
            </div>

            <div style={{ display: "flex", alignItems: "baseline", justifyContent: "center", gap: 16 }}>
              <span style={{ fontSize: 160, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", letterSpacing: "-0.04em", color: "#F8FAFC" }}>
                {humanCount}
              </span>
              <span style={{ fontSize: 84, fontWeight: 800, color: "#38BDF8", fontFamily: "Space Grotesk, sans-serif" }}>
                BILLION
              </span>
            </div>

            <div style={{ fontSize: 32, fontWeight: 600, color: "#94A3B8", marginTop: 8 }}>
              HUMAN BEINGS ON ONE SPINNING BLUE ROCK
            </div>
          </div>

          <div
            style={{
              marginTop: 48,
              width: 140,
              height: 140,
              borderRadius: "50%",
              background: "radial-gradient(circle at 35% 35%, #38BDF8 0%, #0284C7 50%, #0369A1 100%)",
              boxShadow: "0 0 60px rgba(56, 189, 248, 0.4)",
              transform: `rotate(${frame * 0.8}deg)`,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.7)" strokeWidth="1.5">
              <circle cx="12" cy="12" r="10" />
              <path d="M12 2a14.5 14.5 0 0 0 0 20M12 2a14.5 14.5 0 0 1 0 20M2 12h20" />
            </svg>
          </div>
        </div>
      )}

      {/* Part B: 195 Flags & 12,000 Nukes vs 0 Police (650 - 1350) */}
      {frame >= 650 && frame < 1350 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 36 }}>
          <div style={{ display: "flex", gap: 40, alignItems: "center" }}>
            {/* Card 1 */}
            <div
              style={{
                transform: `scale(${card1Spring})`,
                backgroundColor: "rgba(30, 41, 59, 0.9)",
                border: "2px solid #334155",
                borderRadius: 24,
                padding: "36px 48px",
                width: 440,
                textAlign: "center",
                boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
              }}
            >
              <div style={{ fontSize: 18, color: "#94A3B8", fontWeight: 700, letterSpacing: "0.15em", textTransform: "uppercase" }}>
                SOVEREIGN ENTITIES
              </div>
              <div style={{ fontSize: 92, fontWeight: 900, color: "#38BDF8", fontFamily: "Space Grotesk, sans-serif", margin: "12px 0" }}>
                195
              </div>
              <div style={{ fontSize: 20, color: "#CBD5E1", fontWeight: 600 }}>
                Hard borders & finite resources
              </div>
            </div>

            {/* Card 2 */}
            <div
              style={{
                transform: `scale(${card2Spring})`,
                backgroundColor: "rgba(30, 41, 59, 0.9)",
                border: "2px solid #EF444460",
                borderRadius: 24,
                padding: "36px 48px",
                width: 440,
                textAlign: "center",
                boxShadow: "0 20px 40px rgba(0,0,0,0.4)",
              }}
            >
              <div style={{ fontSize: 18, color: "#F87171", fontWeight: 700, letterSpacing: "0.15em", textTransform: "uppercase" }}>
                NUCLEAR ARSENAL
              </div>
              <div style={{ fontSize: 92, fontWeight: 900, color: "#EF4444", fontFamily: "Space Grotesk, sans-serif", margin: "12px 0" }}>
                12,000+
              </div>
              <div style={{ fontSize: 20, color: "#CBD5E1", fontWeight: 600 }}>
                Ready to launch on notice
              </div>
            </div>
          </div>

          {/* Stamp */}
          <div
            style={{
              transform: `scale(${zeroPoliceStamp}) rotate(-3deg)`,
              backgroundColor: "#DC2626",
              color: "#FFFFFF",
              padding: "18px 54px",
              borderRadius: 16,
              fontSize: 38,
              fontWeight: 900,
              fontFamily: "Space Grotesk, sans-serif",
              letterSpacing: "0.08em",
              boxShadow: "0 12px 36px rgba(220, 38, 38, 0.6)",
              border: "3px solid #FEF2F2",
            }}
          >
            GLOBAL POLICE OFFICERS: EXACTLY ZERO
          </div>
        </div>
      )}

      {/* Part C: Domestic Law vs Anarchic Superpowers (1350 - 1850) */}
      {frame >= 1350 && frame < 1850 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div
            style={{
              transform: `scale(${courtSpring})`,
              display: "flex",
              gap: 48,
              maxWidth: 1200,
            }}
          >
            <div
              style={{
                flex: 1,
                backgroundColor: "rgba(30, 41, 59, 0.8)",
                borderRadius: 20,
                padding: 40,
                border: "2px solid #10B98150",
              }}
            >
              <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800, letterSpacing: "0.15em" }}>
                DOMESTIC CONFLICT
              </div>
              <div style={{ fontSize: 32, fontWeight: 800, margin: "16px 0", color: "#F8FAFC" }}>
                Neighbor Disagreements
              </div>
              <div style={{ fontSize: 20, color: "#94A3B8", lineHeight: 1.6 }}>
                You don't build a front-lawn army. You call the municipal police or go to court. A sovereign monopoly on force enforces order.
              </div>
              <div style={{ marginTop: 24, padding: "8px 16px", backgroundColor: "#10B98120", color: "#34D399", borderRadius: 8, display: "inline-block", fontWeight: 700 }}>
                Hierarchical Authority ✓
              </div>
            </div>

            <div
              style={{
                flex: 1,
                backgroundColor: "rgba(30, 41, 59, 0.8)",
                borderRadius: 20,
                padding: 40,
                border: "2px solid #EF444450",
              }}
            >
              <div style={{ fontSize: 16, color: "#EF4444", fontWeight: 800, letterSpacing: "0.15em" }}>
                INTERNATIONAL CONFLICT
              </div>
              <div style={{ fontSize: 32, fontWeight: 800, margin: "16px 0", color: "#F8FAFC" }}>
                Superpower Showdowns
              </div>
              <div style={{ fontSize: 20, color: "#94A3B8", lineHeight: 1.6 }}>
                No global sheriff. No higher court with an army. Who enforces the rules when the dispute is between nuclear-armed nations?
              </div>
              <div style={{ marginTop: 24, padding: "8px 16px", backgroundColor: "#EF444420", color: "#F87171", borderRadius: 8, display: "inline-block", fontWeight: 700 }}>
                No Higher Boss (Anarchy) ✗
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part D: Show Title Stinger (1850 - 2406) */}
      {frame >= 1850 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div style={{ transform: `scale(${stingerSpring})`, textAlign: "center" }}>
            <div
              style={{
                display: "inline-block",
                padding: "8px 24px",
                backgroundColor: "#F59E0B",
                color: "#0F172A",
                fontWeight: 900,
                borderRadius: 9999,
                fontSize: 18,
                letterSpacing: "0.15em",
                marginBottom: 20,
              }}
            >
              EPISODE 01 MASTERCLASS
            </div>

            <h1
              style={{
                fontSize: 84,
                fontWeight: 900,
                fontFamily: "Space Grotesk, sans-serif",
                letterSpacing: "-0.03em",
                margin: 0,
                lineHeight: 1.1,
                color: "#F8FAFC",
              }}
            >
              THE ANARCHY PROBLEM
            </h1>
            <div
              style={{
                fontSize: 36,
                fontWeight: 700,
                color: "#38BDF8",
                marginTop: 16,
                fontFamily: "Space Grotesk, sans-serif",
              }}
            >
              WHO'S IN CHARGE OF THE PLANET?
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 2: WHAT IS ANARCHY? (Frames 2406 - 5871 / 80.2s - 195.7s)
// ===========================================================================
const Act2WhatIsAnarchy: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 800: Hollywood vs Academic Definition
  // 800 - 1700: The Hierarchy Pyramid vs Flat Anarchy
  // 1700 - 2500: Dial 911 Analogy & The UN Reality
  // 2500 - 3465: Self-Help System & Thomas Hobbes

  const defSpring = spring({ frame: frame - 15, fps, config: { damping: 12, stiffness: 100 } });
  const pyramidSpring = spring({ frame: frame - 820, fps, config: { damping: 11, stiffness: 90 } });
  const phoneSpring = spring({ frame: frame - 1720, fps, config: { damping: 12, stiffness: 110 } });
  const hobbesSpring = spring({ frame: frame - 2520, fps, config: { damping: 12, stiffness: 90 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#090D16", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(239, 68, 68, 0.05)" />
      <ActBadge actNum={2} title="What is Anarchy? (No 911 for Nations)" color="#EF4444" />

      {/* Part A: Definition Clarification (0 - 800) */}
      {frame < 800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 32 }}>
          <div style={{ transform: `scale(${defSpring})`, display: "flex", gap: 40, maxWidth: 1200 }}>
            {/* Hollywood */}
            <div
              style={{
                flex: 1,
                backgroundColor: "rgba(30, 41, 59, 0.7)",
                borderRadius: 24,
                padding: 40,
                border: "2px solid #64748B40",
              }}
            >
              <div style={{ fontSize: 16, color: "#94A3B8", fontWeight: 800, letterSpacing: "0.15em" }}>
                HOLLYWOOD DEFINITION
              </div>
              <div style={{ fontSize: 34, fontWeight: 900, color: "#CBD5E1", margin: "16px 0" }}>
                Mad Max Pandemonium
              </div>
              <div style={{ fontSize: 20, color: "#94A3B8", lineHeight: 1.6 }}>
                Burning cars, masked rioters in the streets, fighting over the last can of beans in a post-apocalyptic wasteland.
              </div>
            </div>

            {/* IR Definition */}
            <div
              style={{
                flex: 1,
                backgroundColor: "rgba(30, 41, 59, 0.9)",
                borderRadius: 24,
                padding: 40,
                border: "2px solid #EF4444",
                boxShadow: "0 0 40px rgba(239, 68, 68, 0.2)",
              }}
            >
              <div style={{ fontSize: 16, color: "#EF4444", fontWeight: 800, letterSpacing: "0.15em" }}>
                IR SCIENTIFIC DEFINITION
              </div>
              <div style={{ fontSize: 34, fontWeight: 900, color: "#F8FAFC", margin: "16px 0" }}>
                Absence of Central Ruler
              </div>
              <div style={{ fontSize: 20, color: "#E2E8F0", lineHeight: 1.6 }}>
                The lack of an overarching global government with sovereign power to enforce binding international laws.
              </div>
            </div>
          </div>

          <div
            style={{
              padding: "12px 32px",
              backgroundColor: "#EF444420",
              border: "1px solid #EF444460",
              borderRadius: 9999,
              color: "#FCA5A5",
              fontSize: 22,
              fontWeight: 800,
            }}
          >
            ANARCHY ≠ CHAOS. IT MEANS NO GLOBAL SOVEREIGN.
          </div>
        </div>
      )}

      {/* Part B: Pyramid vs Flat Plane (800 - 1700) */}
      {frame >= 800 && frame < 1700 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div style={{ transform: `scale(${pyramidSpring})`, display: "flex", gap: 60, alignItems: "center" }}>
            {/* Pyramid */}
            <div style={{ textAlign: "center", width: 480 }}>
              <div style={{ fontSize: 22, fontWeight: 800, color: "#38BDF8", marginBottom: 20 }}>
                DOMESTIC POLITICS = PYRAMID
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: 10, alignItems: "center" }}>
                <div style={{ width: 180, padding: "16px 0", backgroundColor: "#0284C7", color: "#FFFFFF", fontWeight: 900, borderRadius: 8 }}>
                  Constitution & Apex
                </div>
                <div style={{ width: 300, padding: "16px 0", backgroundColor: "#0369A1", color: "#FFFFFF", fontWeight: 800, borderRadius: 8 }}>
                  Police & Judiciary
                </div>
                <div style={{ width: 420, padding: "18px 0", backgroundColor: "#075985", color: "#FFFFFF", fontWeight: 700, borderRadius: 8 }}>
                  Protected Citizens
                </div>
              </div>
              <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 16 }}>
                Clear vertical monopoly on legitimate force
              </div>
            </div>

            {/* Flat Plane */}
            <div style={{ textAlign: "center", width: 480 }}>
              <div style={{ fontSize: 22, fontWeight: 800, color: "#F59E0B", marginBottom: 20 }}>
                INTERNATIONAL POLITICS = FLAT
              </div>
              <div style={{ display: "flex", justifyContent: "center", gap: 16, padding: "40px 20px", border: "2px dashed #475569", borderRadius: 16 }}>
                {["USA", "CHN", "GBR", "FRA", "IDN", "IND"].map((code) => (
                  <div key={code} style={{ padding: "16px 12px", backgroundColor: "#334155", color: "#F8FAFC", fontWeight: 800, borderRadius: 8 }}>
                    {code}
                  </div>
                ))}
              </div>
              <div style={{ fontSize: 16, color: "#F59E0B", marginTop: 24, fontWeight: 700 }}>
                Zero Sovereign Apex. All states legally sovereign & co-equal.
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part C: Dial 911 & The UN (1700 - 2500) */}
      {frame >= 1700 && frame < 2500 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 32 }}>
          <div
            style={{
              transform: `scale(${phoneSpring})`,
              backgroundColor: "rgba(30, 41, 59, 0.9)",
              borderRadius: 24,
              border: "2px solid #EF4444",
              padding: "40px 60px",
              textAlign: "center",
              maxWidth: 900,
            }}
          >
            <div style={{ fontSize: 72, fontWeight: 900, color: "#EF4444", letterSpacing: "0.05em" }}>
              DIAL 9-1-1 ?
            </div>
            <div style={{ fontSize: 32, fontWeight: 800, color: "#F8FAFC", margin: "16px 0" }}>
              THERE IS NO 911 FOR SOVEREIGN NATIONS
            </div>
            <div style={{ fontSize: 20, color: "#94A3B8", lineHeight: 1.6 }}>
              The United Nations is not a world government. It has no standing army of its own, cannot arrest superpowers, and cannot override sovereign constitutional vetoes.
            </div>
          </div>
        </div>
      )}

      {/* Part D: Self-Help & Thomas Hobbes (2500 - 3465) */}
      {frame >= 2500 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div
            style={{
              transform: `scale(${hobbesSpring})`,
              backgroundColor: "rgba(15, 23, 42, 0.95)",
              borderRadius: 24,
              border: "2px solid #F59E0B60",
              padding: "48px 64px",
              maxWidth: 1000,
              boxShadow: "0 20px 50px rgba(0,0,0,0.5)",
            }}
          >
            <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE STATE OF NATURE // THOMAS HOBBES (1651)
            </div>
            <div
              style={{
                fontSize: 34,
                fontWeight: 700,
                color: "#FEF3C7",
                fontStyle: "italic",
                lineHeight: 1.5,
              }}
            >
              "Without a common power to keep them all in awe, life is solitary, poor, nasty, brutish, and short."
            </div>
            <div style={{ marginTop: 28, display: "flex", gap: 16, alignItems: "center" }}>
              <span style={{ backgroundColor: "#F59E0B", color: "#0F172A", fontWeight: 900, padding: "8px 16px", borderRadius: 8, fontSize: 16 }}>
                THE RESULT
              </span>
              <span style={{ fontSize: 22, color: "#E2E8F0", fontWeight: 700 }}>
                A Perpetual Self-Help System where survival depends on your own power & alliances.
              </span>
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 3: ANATOMY OF THE SOVEREIGN STATE (Frames 5871 - 9618 / 195.7s - 320.6s)
// ===========================================================================
const Act3SovereignState: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 900: Country vs Nation vs State
  // 900 - 2100: Montevideo Convention (1933) 4 Pillars
  // 2100 - 3747: Peace of Westphalia (1648) & Non-Intervention

  const triSpring = spring({ frame: frame - 15, fps, config: { damping: 12, stiffness: 100 } });
  const monteSpring = spring({ frame: frame - 920, fps, config: { damping: 11, stiffness: 90 } });
  const westSpring = spring({ frame: frame - 2120, fps, config: { damping: 12, stiffness: 100 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0C1222", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(16, 185, 129, 0.05)" />
      <ActBadge actNum={3} title="Anatomy of the Sovereign State" color="#10B981" />

      {/* Part A: Country vs Nation vs State (0 - 900) */}
      {frame < 900 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 32 }}>
          <div style={{ transform: `scale(${triSpring})`, display: "flex", gap: 32, maxWidth: 1280 }}>
            {/* Country */}
            <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 20, padding: 32, border: "2px solid #38BDF850" }}>
              <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800 }}>GEOGRAPHIC</div>
              <div style={{ fontSize: 32, fontWeight: 900, margin: "12px 0", color: "#F8FAFC" }}>Country</div>
              <div style={{ fontSize: 18, color: "#94A3B8", lineHeight: 1.5 }}>
                A geographic territory with physical land, rivers, and borders (e.g. New Zealand).
              </div>
            </div>

            {/* Nation */}
            <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 20, padding: 32, border: "2px solid #F59E0B50" }}>
              <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800 }}>CULTURAL</div>
              <div style={{ fontSize: 32, fontWeight: 900, margin: "12px 0", color: "#F8FAFC" }}>Nation</div>
              <div style={{ fontSize: 18, color: "#94A3B8", lineHeight: 1.5 }}>
                A group of people sharing common culture, language, and identity (e.g. Kurds, Basques).
              </div>
            </div>

            {/* State */}
            <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.9)", borderRadius: 20, padding: 32, border: "2px solid #10B981", boxShadow: "0 0 30px rgba(16, 185, 129, 0.2)" }}>
              <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>POLITICAL & LEGAL</div>
              <div style={{ fontSize: 32, fontWeight: 900, margin: "12px 0", color: "#F8FAFC" }}>State</div>
              <div style={{ fontSize: 18, color: "#E2E8F0", lineHeight: 1.5 }}>
                A formal political entity exercising supreme legal jurisdiction and monopoly on force.
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part B: Montevideo Convention 1933 (900 - 2100) */}
      {frame >= 900 && frame < 2100 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 24 }}>
          <div style={{ transform: `scale(${monteSpring})`, textAlign: "center", maxWidth: 1100 }}>
            <div style={{ fontSize: 20, color: "#10B981", fontWeight: 800, letterSpacing: "0.15em", marginBottom: 8 }}>
              MONTEVIDEO CONVENTION (1933)
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", marginBottom: 32 }}>
              THE 4 GOLDEN PILLARS OF STATEHOOD
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, borderLeft: "6px solid #10B981", textAlign: "left" }}>
                <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>PILLAR 1</div>
                <div style={{ fontSize: 24, fontWeight: 800, color: "#F8FAFC", marginTop: 4 }}>Permanent Population</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 6 }}>Cannot be a deserted rock or seasonal tourist campsite.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, borderLeft: "6px solid #10B981", textAlign: "left" }}>
                <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>PILLAR 2</div>
                <div style={{ fontSize: 24, fontWeight: 800, color: "#F8FAFC", marginTop: 4 }}>Defined Territory</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 6 }}>Borders that you effectively govern and control.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, borderLeft: "6px solid #10B981", textAlign: "left" }}>
                <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>PILLAR 3</div>
                <div style={{ fontSize: 24, fontWeight: 800, color: "#F8FAFC", marginTop: 4 }}>Functioning Government</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 6 }}>Capable of maintaining domestic legal order.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.9)", padding: 24, borderRadius: 16, borderLeft: "6px solid #F59E0B", textAlign: "left", boxShadow: "0 0 20px rgba(245, 158, 11, 0.2)" }}>
                <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800 }}>PILLAR 4 (CRITICAL)</div>
                <div style={{ fontSize: 24, fontWeight: 800, color: "#FEF3C7", marginTop: 4 }}>Diplomatic Recognition</div>
                <div style={{ fontSize: 16, color: "#CBD5E1", marginTop: 6 }}>Capacity to enter relations with other sovereign states.</div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part C: Peace of Westphalia 1648 (2100 - 3747) */}
      {frame >= 2100 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div
            style={{
              transform: `scale(${westSpring})`,
              backgroundColor: "rgba(15, 23, 42, 0.95)",
              borderRadius: 24,
              border: "2px solid #10B98160",
              padding: "48px 64px",
              maxWidth: 1050,
              boxShadow: "0 20px 50px rgba(0,0,0,0.5)",
            }}
          >
            <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE BIRTH OF SOVEREIGNTY // PEACE OF WESTPHALIA (1648)
            </div>
            <div style={{ fontSize: 40, fontWeight: 900, color: "#F8FAFC", lineHeight: 1.2 }}>
              "Rex in regno suo est imperator"
            </div>
            <div style={{ fontSize: 24, color: "#F59E0B", fontWeight: 700, marginTop: 8 }}>
              The King is Emperor Within His Own Realm
            </div>
            <div style={{ fontSize: 20, color: "#94A3B8", marginTop: 24, lineHeight: 1.6 }}>
              No foreign pope, rival king, or external emperor has the legal right to dictate domestic policy.
              Borders became sacred, non-intervention became the supreme global norm.
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 4: NON-STATE TITANS (Frames 9618 - 13351 / 320.6s - 445.0s)
// ===========================================================================
const Act4NonStateTitans: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 1200: Apple ($3 Trillion) vs National GDP
  // 1200 - 2400: Regulatory Arbitrage & Capital Flight
  // 2400 - 3733: INGOs & Moral Normative Power vs Cyber Cartels

  const appleSpring = spring({ frame: frame - 15, fps, config: { damping: 12, stiffness: 100 } });
  const arbSpring = spring({ frame: frame - 1220, fps, config: { damping: 11, stiffness: 90 } });
  const ingoSpring = spring({ frame: frame - 2420, fps, config: { damping: 12, stiffness: 100 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0A101D", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(139, 92, 246, 0.05)" />
      <ActBadge actNum={4} title="Non-State Titans: Tech, Capital, and Citizens" color="#8B5CF6" />

      {/* Part A: Apple vs Nations (0 - 1200) */}
      {frame < 1200 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 32 }}>
          <div style={{ transform: `scale(${appleSpring})`, textAlign: "center", maxWidth: 1100 }}>
            <div style={{ fontSize: 18, color: "#A78BFA", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              CORPORATE POWER VS NATION-STATES
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", marginBottom: 32 }}>
              APPLE'S $3 TRILLION BALANCE SHEET
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: 14, width: 800, margin: "0 auto" }}>
              {[
                { name: "France GDP", val: "$3.05 Trillion", width: "95%", color: "#64748B" },
                { name: "Apple Inc. (Market Cap)", val: "$3.00 Trillion", width: "93%", color: "#8B5CF6", highlight: true },
                { name: "Italy GDP", val: "$2.25 Trillion", width: "70%", color: "#64748B" },
                { name: "Brazil GDP", val: "$2.17 Trillion", width: "67%", color: "#64748B" },
                { name: "Canada GDP", val: "$2.14 Trillion", width: "66%", color: "#64748B" },
              ].map((item, idx) => (
                <div key={idx} style={{ display: "flex", alignItems: "center", gap: 16 }}>
                  <div style={{ width: 220, textAlign: "right", fontSize: 18, fontWeight: item.highlight ? 900 : 600, color: item.highlight ? "#FEF3C7" : "#CBD5E1" }}>
                    {item.name}
                  </div>
                  <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.6)", borderRadius: 8, overflow: "hidden", height: 38 }}>
                    <div style={{ width: item.width, height: "100%", backgroundColor: item.color, display: "flex", alignItems: "center", paddingLeft: 16, fontWeight: 800, fontSize: 16, color: "#FFFFFF" }}>
                      {item.val}
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <div style={{ marginTop: 24, fontSize: 20, color: "#C4B5FD", fontWeight: 700 }}>
              Apple would be the 7th largest economy on planet Earth.
            </div>
          </div>
        </div>
      )}

      {/* Part B: Regulatory Arbitrage (1200 - 2400) */}
      {frame >= 1200 && frame < 2400 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 32 }}>
          <div
            style={{
              transform: `scale(${arbSpring})`,
              backgroundColor: "rgba(30, 41, 59, 0.8)",
              borderRadius: 24,
              border: "2px solid #8B5CF6",
              padding: "40px 60px",
              textAlign: "center",
              maxWidth: 950,
            }}
          >
            <div style={{ fontSize: 16, color: "#A78BFA", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              ECONOMIC PHENOMENON
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", marginBottom: 16 }}>
              REGULATORY ARBITRAGE
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", lineHeight: 1.6 }}>
              Capital moves with a keystroke. Multinationals shift manufacturing, profits, and intellectual property across borders to whichever country offers the lowest corporate taxes and loosest environmental laws.
            </div>
            <div style={{ marginTop: 28, padding: "12px 28px", backgroundColor: "#8B5CF620", color: "#C4B5FD", borderRadius: 12, display: "inline-block", fontWeight: 800, fontSize: 18 }}>
              States compete to keep corporations happy, not vice versa.
            </div>
          </div>
        </div>
      )}

      {/* Part C: INGOs & Soft Power (2400 - 3733) */}
      {frame >= 2400 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div style={{ transform: `scale(${ingoSpring})`, display: "flex", gap: 36, maxWidth: 1150 }}>
            {/* INGOs */}
            <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 20, padding: 36, border: "2px solid #10B98150" }}>
              <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>TRANSNATIONAL CIVIL SOCIETY</div>
              <div style={{ fontSize: 28, fontWeight: 900, color: "#F8FAFC", margin: "14px 0" }}>INGOs & Moral Soft Power</div>
              <div style={{ fontSize: 18, color: "#94A3B8", lineHeight: 1.6 }}>
                Amnesty, Greenpeace, Doctors Without Borders. No aircraft carriers, but vast moral authority to shame sovereign states into changing policies.
              </div>
            </div>

            {/* Illicit Actors */}
            <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 20, padding: 36, border: "2px solid #EF444450" }}>
              <div style={{ fontSize: 16, color: "#EF4444", fontWeight: 800 }}>ASYMMETRIC THREATS</div>
              <div style={{ fontSize: 28, fontWeight: 900, color: "#F8FAFC", margin: "14px 0" }}>Cartels & Cyber Syndicates</div>
              <div style={{ fontSize: 18, color: "#94A3B8", lineHeight: 1.6 }}>
                Transnational gangs and state-sponsored hackers exploit open global seams to strike critical infrastructure without declaring formal war.
              </div>
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 5: THE CORE PARADOX (Frames 13351 - 16998 / 445.0s - 566.6s)
// ===========================================================================
const Act5TheParadox: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 800: The Tuesday Afternoon Paradox
  // 800 - 1800: Realism Corner: Balance of Power & MAD
  // 1800 - 2800: Liberalism Corner: Complex Interdependence (Smartphone)
  // 2800 - 3647: International Institutions as Friction Reducers

  const parSpring = spring({ frame: frame - 15, fps, config: { damping: 12, stiffness: 100 } });
  const realSpring = spring({ frame: frame - 820, fps, config: { damping: 11, stiffness: 90 } });
  const libSpring = spring({ frame: frame - 1820, fps, config: { damping: 12, stiffness: 100 } });
  const instSpring = spring({ frame: frame - 2820, fps, config: { damping: 12, stiffness: 90 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0B111E", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(6, 182, 212, 0.05)" />
      <ActBadge actNum={5} title="The Core Paradox: Why Isn't the World Constantly at War?" color="#06B6D4" />

      {/* Part A: The Paradox (0 - 800) */}
      {frame < 800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 24 }}>
          <div style={{ transform: `scale(${parSpring})`, textAlign: "center", maxWidth: 1000 }}>
            <div style={{ fontSize: 18, color: "#06B6D4", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE CENTRAL MYSTERY OF IR
            </div>
            <div style={{ fontSize: 52, fontWeight: 900, color: "#F8FAFC", lineHeight: 1.15 }}>
              WHY ISN'T THE WORLD AT WAR EVERY SINGLE TUESDAY?
            </div>
            <div style={{ fontSize: 24, color: "#94A3B8", marginTop: 20, lineHeight: 1.5 }}>
              100,000 international flights land safely each morning. Container ships crisscross oceans unmolested. If anarchy is real, why does cooperation exist?
            </div>
          </div>
        </div>
      )}

      {/* Part B: Realism Corner (800 - 1800) */}
      {frame >= 800 && frame < 1800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div
            style={{
              transform: `scale(${realSpring})`,
              backgroundColor: "rgba(30, 41, 59, 0.9)",
              borderRadius: 24,
              border: "2px solid #EF4444",
              padding: "44px 64px",
              maxWidth: 950,
              boxShadow: "0 20px 40px rgba(239, 68, 68, 0.2)",
            }}
          >
            <div style={{ fontSize: 16, color: "#EF4444", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              THE REALIST EXPLANATION
            </div>
            <div style={{ fontSize: 40, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>
              Balance of Power & Nuclear Deterrence
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", lineHeight: 1.6 }}>
              Peace is just the temporary intermission between wars. States do not attack because attacking risks Mutually Assured Destruction (MAD).
            </div>
            <div style={{ marginTop: 24, padding: "10px 24px", backgroundColor: "#EF444420", color: "#FCA5A5", borderRadius: 8, display: "inline-block", fontWeight: 800, fontSize: 18 }}>
              Fear, not friendship, keeps the weapons holstered.
            </div>
          </div>
        </div>
      )}

      {/* Part C: Liberalism & Complex Interdependence (1800 - 2800) */}
      {frame >= 1800 && frame < 2800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 28 }}>
          <div style={{ transform: `scale(${libSpring})`, textAlign: "center", maxWidth: 1100 }}>
            <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              THE LIBERAL EXPLANATION
            </div>
            <div style={{ fontSize: 40, fontWeight: 900, color: "#F8FAFC", marginBottom: 24 }}>
              COMPLEX INTERDEPENDENCE (THE SMARTPHONE TEST)
            </div>

            <div style={{ display: "flex", gap: 20, justifyContent: "center" }}>
              {[
                { part: "Design & Software", loc: "California, USA" },
                { part: "Silicon Microchips", loc: "TSMC, Taiwan" },
                { part: "Display & Batteries", loc: "Seoul, South Korea" },
                { part: "Cobalt & Rare Earths", loc: "DR Congo & China" },
              ].map((item, idx) => (
                <div key={idx} style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: "20px 24px", borderRadius: 16, borderTop: "4px solid #38BDF8", width: 220 }}>
                  <div style={{ fontSize: 14, color: "#94A3B8", fontWeight: 700 }}>{item.part}</div>
                  <div style={{ fontSize: 18, color: "#F8FAFC", fontWeight: 800, marginTop: 6 }}>{item.loc}</div>
                </div>
              ))}
            </div>

            <div style={{ marginTop: 28, fontSize: 22, color: "#7DD3FC", fontWeight: 700 }}>
              Going to war with your major trade partner is economic suicide.
            </div>
          </div>
        </div>
      )}

      {/* Part D: Institutions as Friction Reducers (2800 - 3647) */}
      {frame >= 2800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%" }}>
          <div
            style={{
              transform: `scale(${instSpring})`,
              backgroundColor: "rgba(30, 41, 59, 0.9)",
              borderRadius: 24,
              border: "2px solid #06B6D4",
              padding: "44px 64px",
              maxWidth: 980,
            }}
          >
            <div style={{ fontSize: 16, color: "#06B6D4", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              GLOBAL GOVERNANCE
            </div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>
              International Organizations as Friction-Reducers
            </div>
            <div style={{ fontSize: 20, color: "#CBD5E1", lineHeight: 1.6 }}>
              The WTO, the International Maritime Organization, and international courts set standardized rules of the road.
              They lower the cost of making agreements, monitor compliance, and tame the anarchy beast through diplomacy.
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 6: THE TAKEAWAY (Frames 16998 - 19368 / 566.6s - 645.6s)
// ===========================================================================
const Act6TheTakeaway: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Sub-segments:
  // 0 - 800: IR in Daily Life
  // 800 - 1600: The 4 Episode Pillars
  // 1600 - 2370: Channel Sign-off & Lesson Completed

  const dailySpring = spring({ frame: frame - 15, fps, config: { damping: 12, stiffness: 100 } });
  const pillarsSpring = spring({ frame: frame - 820, fps, config: { damping: 11, stiffness: 90 } });
  const outroSpring = spring({ frame: frame - 1620, fps, config: { damping: 12, stiffness: 100 } });

  return (
    <AbsoluteFill style={{ backgroundColor: "#0F172A", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(245, 158, 11, 0.05)" />
      <ActBadge actNum={6} title="The Takeaway: Why IR Matters to You" color="#F59E0B" />

      {/* Part A: Daily Life Impact (0 - 800) */}
      {frame < 800 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 28 }}>
          <div style={{ transform: `scale(${dailySpring})`, textAlign: "center", maxWidth: 1100 }}>
            <div style={{ fontSize: 18, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              THE INVISIBLE OPERATING SYSTEM
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", marginBottom: 28 }}>
              IR RUNS IN THE BACKGROUND OF YOUR DAILY LIFE
            </div>

            <div style={{ display: "flex", gap: 24, justifyContent: "center" }}>
              <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 16, padding: 24, borderTop: "4px solid #EF4444" }}>
                <div style={{ fontSize: 16, color: "#F87171", fontWeight: 800 }}>Strait of Hormuz</div>
                <div style={{ fontSize: 18, color: "#E2E8F0", marginTop: 8 }}>Directly dictates gas prices at your local pump.</div>
              </div>

              <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 16, padding: 24, borderTop: "4px solid #38BDF8" }}>
                <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800 }}>Tech Tariff Wars</div>
                <div style={{ fontSize: 18, color: "#E2E8F0", marginTop: 8 }}>Shifts the price of your next smartphone or laptop.</div>
              </div>

              <div style={{ flex: 1, backgroundColor: "rgba(30, 41, 59, 0.8)", borderRadius: 16, padding: 24, borderTop: "4px solid #10B981" }}>
                <div style={{ fontSize: 16, color: "#34D399", fontWeight: 800 }}>Global Climate Pacts</div>
                <div style={{ fontSize: 18, color: "#E2E8F0", marginTop: 8 }}>Determines environmental stability for the next century.</div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part B: 4 Pillars of Episode 1 (800 - 1600) */}
      {frame >= 800 && frame < 1600 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 24 }}>
          <div style={{ transform: `scale(${pillarsSpring})`, textAlign: "center", maxWidth: 1100 }}>
            <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              EPISODE 01 CORE TAKEAWAYS
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", marginBottom: 28 }}>
              YOUR 4 FOUNDATION CONCEPTS
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, textAlign: "left", border: "1px solid #334155" }}>
                <div style={{ fontSize: 22, fontWeight: 800, color: "#EF4444" }}>1. ANARCHY</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>The absence of a central world government.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, textAlign: "left", border: "1px solid #334155" }}>
                <div style={{ fontSize: 22, fontWeight: 800, color: "#10B981" }}>2. SOVEREIGNTY</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>Supreme legal authority within defined territorial borders.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, textAlign: "left", border: "1px solid #334155" }}>
                <div style={{ fontSize: 22, fontWeight: 800, color: "#38BDF8" }}>3. STATE</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>The primary legal actor on the international stage.</div>
              </div>

              <div style={{ backgroundColor: "rgba(30, 41, 59, 0.8)", padding: 24, borderRadius: 16, textAlign: "left", border: "1px solid #334155" }}>
                <div style={{ fontSize: 22, fontWeight: 800, color: "#F59E0B" }}>4. INTERDEPENDENCE</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>The complex web of trade & rules that keeps catastrophic war at bay.</div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Part C: Lesson Completed & Channel Outro (1600 - 2370) */}
      {frame >= 1600 && (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", gap: 28 }}>
          <div
            style={{
              transform: `scale(${outroSpring})`,
              backgroundColor: "rgba(15, 23, 42, 0.95)",
              borderRadius: 24,
              border: "2px solid #F59E0B",
              padding: "48px 80px",
              textAlign: "center",
              boxShadow: "0 20px 60px rgba(245, 158, 11, 0.25)",
            }}
          >
            <div
              style={{
                display: "inline-block",
                padding: "8px 20px",
                backgroundColor: "#F59E0B",
                color: "#0F172A",
                fontWeight: 900,
                borderRadius: 9999,
                fontSize: 16,
                letterSpacing: "0.15em",
                marginBottom: 16,
              }}
            >
              LESSON 01 COMPLETE ✓
            </div>
            <div style={{ fontSize: 52, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", color: "#F8FAFC" }}>
              CRASH COURSE IR #1
            </div>
            <div style={{ fontSize: 26, color: "#38BDF8", fontWeight: 700, marginTop: 8 }}>
              SEE YOU NEXT TIME ON @IRinANutshell
            </div>
            <div style={{ fontSize: 18, color: "#94A3B8", marginTop: 20 }}>
              Next Up: Realism vs Liberalism — The Great Theoretical Showdown
            </div>
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// MASTER COMPOSITION: CrashCourseIR10Min (19,368 Frames @ 30 FPS = 10m 45.6s)
// ===========================================================================
export const CrashCourse10MinComposition: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#000000", overflow: "hidden" }}>
      {/* Background BGM Loop: Upbeat Acoustic/Indie Vibe */}
      <Loop durationInFrames={1200}>
        <Audio src={staticFile("assets/vox_bgm.aac")} volume={0.22} />
      </Loop>

      {/* Main Kokoro-82M Voice Track (am_adam, 645.6s) */}
      <Audio src={staticFile("assets/crashcourse_10min_kokoro.mp3")} volume={1.35} />

      {/* ACT 1: The Hook & The Great Illusion (0 - 2406 frames / 80.2s) */}
      <Sequence from={0} durationInFrames={2406}>
        <Act1TheHook />
      </Sequence>

      {/* ACT 2: What is Anarchy? (2406 - 5871 frames / 115.5s) */}
      <Sequence from={2406} durationInFrames={3465}>
        <Act2WhatIsAnarchy />
      </Sequence>

      {/* ACT 3: Anatomy of the Sovereign State (5871 - 9618 frames / 124.9s) */}
      <Sequence from={5871} durationInFrames={3747}>
        <Act3SovereignState />
      </Sequence>

      {/* ACT 4: Non-State Titans (9618 - 13351 frames / 124.4s) */}
      <Sequence from={9618} durationInFrames={3733}>
        <Act4NonStateTitans />
      </Sequence>

      {/* ACT 5: The Core Paradox (13351 - 16998 frames / 121.6s) */}
      <Sequence from={13351} durationInFrames={3647}>
        <Act5TheParadox />
      </Sequence>

      {/* ACT 6: The Takeaway & Outro (16998 - 19368 frames / 79.0s) */}
      <Sequence from={16998} durationInFrames={2370}>
        <Act6TheTakeaway />
      </Sequence>

      {/* Synchronized Word-Level Karaoke Subtitle Overlay (1,778 words) */}
      <CaptionOverlay
        words={wordTimestamps}
        wordsPerPage={5}
        fontSize={40}
        color="#F8FAFC"
        highlightColor="#F59E0B"
        backgroundColor="rgba(15, 23, 42, 0.85)"
      />
    </AbsoluteFill>
  );
};
'''

with open(TSX_PATH, "w", encoding="utf-8") as f:
    f.write(CONTENT)

print(f"Successfully generated {TSX_PATH} ({len(CONTENT)} bytes)!")
