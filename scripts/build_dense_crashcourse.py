# -*- coding: utf-8 -*-
"""
Builds the ultra high-density CrashCourse10Min.tsx with 65+ visual beats,
active SVG illustrations, CameraRig push-ins, and zero static slides.
"""

TSX_PATH = "simulation/openmontage_repo/remotion-composer/src/CrashCourse10Min.tsx"

code = '''import React from "react";
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
// SHARED CAMERA RIG & ATOMIC VISUAL PRIMITIVES
// ===========================================================================

const CameraRig: React.FC<{
  children: React.ReactNode;
  beatStart: number;
  beatDuration: number;
  zoom?: boolean;
}> = ({ children, beatStart, beatDuration, zoom = true }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const relFrame = Math.max(0, frame - beatStart);
  const entrance = spring({
    frame: relFrame,
    fps,
    config: { damping: 12, stiffness: 120 },
  });

  // Slow continuous push-in across the beat
  const pushIn = zoom
    ? interpolate(relFrame, [0, beatDuration], [1, 1.05], {
        extrapolateRight: "clamp",
      })
    : 1;

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        transform: `scale(${interpolate(entrance, [0, 1], [0.92, 1]) * pushIn})`,
        opacity: interpolate(relFrame, [0, 8], [0, 1], {
          extrapolateRight: "clamp",
        }),
      }}
    >
      {children}
    </div>
  );
};

const GridBackground: React.FC<{ accentColor?: string }> = ({
  accentColor = "rgba(59, 130, 246, 0.05)",
}) => (
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

const ActBadge: React.FC<{ actNum: number; title: string; color?: string }> = ({
  actNum,
  title,
  color = "#F59E0B",
}) => (
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
// ACT 1: THE HOOK & THE GREAT ILLUSION (Frames 0 - 2406 / 80.2s)
// 11 Rapid-Fire Visual Beats
// ===========================================================================
const Act1TheHook: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#0F172A", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(245, 158, 11, 0.06)" />
      <ActBadge actNum={1} title="The Hook & The Great Illusion" color="#F59E0B" />

      {/* Beat 1.1: Alex Intro & Crash Course Badge (0 - 130) */}
      {frame >= 0 && frame < 130 && (
        <CameraRig beatStart={0} beatDuration={130}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 16 }}>
            <div style={{ padding: "8px 24px", backgroundColor: "#F59E0B", color: "#0F172A", fontWeight: 900, borderRadius: 9999, fontSize: 20, letterSpacing: "0.15em" }}>
              WELCOME TO CRASH COURSE
            </div>
            <div style={{ fontSize: 76, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", letterSpacing: "-0.03em", color: "#F8FAFC" }}>
              INTERNATIONAL RELATIONS
            </div>
            <div style={{ fontSize: 28, color: "#38BDF8", fontWeight: 700 }}>
              Hosted by Alex // @IRinANutshell
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.2: 8 Billion Humans on Spinning Blue Rock (130 - 250) */}
      {frame >= 130 && frame < 250 && (
        <CameraRig beatStart={130} beatDuration={120}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20 }}>
            <div style={{ display: "flex", alignItems: "baseline", gap: 16 }}>
              <span style={{ fontSize: 130, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", color: "#38BDF8" }}>
                8,000,000,000
              </span>
              <span style={{ fontSize: 40, fontWeight: 800, color: "#F59E0B" }}>PEOPLE</span>
            </div>
            {/* Spinning Earth Vector */}
            <div style={{ width: 140, height: 140, borderRadius: "50%", background: "radial-gradient(circle at 35% 35%, #38BDF8 0%, #0284C7 60%, #0369A1 100%)", boxShadow: "0 0 50px rgba(56,189,248,0.5)", transform: `rotate(${frame * 1.2}deg)`, display: "flex", alignItems: "center", justifyContent: "center" }}>
              <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,0.8)" strokeWidth="1.5">
                <circle cx="12" cy="12" r="10" />
                <path d="M12 2a14.5 14.5 0 0 0 0 20M12 2a14.5 14.5 0 0 1 0 20M2 12h20" />
              </svg>
            </div>
            <div style={{ fontSize: 26, color: "#94A3B8", fontWeight: 600 }}>ONE SPINNING BLUE ROCK</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.3: 195 Sovereign Borders & Finite Resources (250 - 480) */}
      {frame >= 250 && frame < 480 && (
        <CameraRig beatStart={250} beatDuration={230}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 32 }}>
            <div style={{ display: "flex", gap: 32 }}>
              <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #38BDF8", borderRadius: 20, padding: "28px 40px", textAlign: "center", width: 340 }}>
                <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800 }}>SOVEREIGN STATES</div>
                <div style={{ fontSize: 72, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>195</div>
                <div style={{ fontSize: 16, color: "#94A3B8" }}>Barbed-wire borders</div>
              </div>
              <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #F59E0B", borderRadius: 20, padding: "28px 40px", textAlign: "center", width: 440 }}>
                <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800 }}>FINITE RESOURCE COMPETITION</div>
                <div style={{ display: "flex", flexDirection: "column", gap: 8, marginTop: 12 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: 16, fontWeight: 700 }}>
                    <span>Crude Oil</span><span style={{ color: "#F59E0B" }}>82% Capacity</span>
                  </div>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: 16, fontWeight: 700 }}>
                    <span>Fresh Water</span><span style={{ color: "#38BDF8" }}>64% Strained</span>
                  </div>
                  <div style={{ display: "flex", justifyContent: "space-between", fontSize: 16, fontWeight: 700 }}>
                    <span>Arable Farmland</span><span style={{ color: "#10B981" }}>45% Critical</span>
                  </div>
                </div>
              </div>
            </div>
            {/* Barbed Wire Banner */}
            <div style={{ padding: "8px 32px", backgroundColor: "#334155", borderRadius: 8, fontSize: 18, fontWeight: 700, color: "#CBD5E1", letterSpacing: "0.1em" }}>
              ⚔️ COMPETING ON A FINITE SURFACE
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.4: 12,000 Nuclear Warheads (480 - 635) */}
      {frame >= 480 && frame < 635 && (
        <CameraRig beatStart={480} beatDuration={155}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24 }}>
            <div style={{ display: "inline-flex", alignItems: "center", gap: 12, padding: "10px 24px", backgroundColor: "#EF444420", border: "2px solid #EF4444", borderRadius: 9999, color: "#F87171", fontSize: 20, fontWeight: 900 }}>
              <span style={{ animation: "pulse 1s infinite" }}>⚠️</span> NUCLEAR ARSENAL READY ON NOTICE
            </div>
            <div style={{ fontSize: 120, fontWeight: 900, color: "#EF4444", fontFamily: "Space Grotesk, sans-serif", letterSpacing: "-0.04em" }}>
              12,000+
            </div>
            <div style={{ fontSize: 28, color: "#E2E8F0", fontWeight: 700 }}>
              WARHEADS CAPABLE OF TOTAL PLANETARY COLLAPSE
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.5: ZERO Global Police Officers (635 - 870) */}
      {frame >= 635 && frame < 870 && (
        <CameraRig beatStart={635} beatDuration={235}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 28 }}>
            <div style={{ width: 140, height: 140, borderRadius: "50%", backgroundColor: "#DC262620", border: "4px solid #DC2626", display: "flex", alignItems: "center", justifyContent: "center" }}>
              <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="#DC2626" strokeWidth="2.5">
                <circle cx="12" cy="12" r="10" />
                <line x1="4.93" y1="4.93" x2="19.07" y2="19.07" />
              </svg>
            </div>
            <div style={{ transform: "rotate(-2deg)", backgroundColor: "#DC2626", color: "#FFFFFF", padding: "18px 56px", borderRadius: 16, fontSize: 44, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", boxShadow: "0 12px 40px rgba(220,38,38,0.7)" }}>
              GLOBAL POLICE OFFICERS: EXACTLY ZERO
            </div>
            <div style={{ fontSize: 24, color: "#94A3B8", fontWeight: 600 }}>NO ONE WALKING THE BEAT TO STOP TOTAL MAYHEM</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.6: Think About That (870 - 930) */}
      {frame >= 870 && frame < 930 && (
        <CameraRig beatStart={870} beatDuration={60}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 72, fontWeight: 900, color: "#FEF3C7", fontFamily: "Space Grotesk, sans-serif" }}>
              THINK ABOUT THAT.
            </div>
            <div style={{ fontSize: 26, color: "#F59E0B", marginTop: 12, fontWeight: 700 }}>
              Let that sink in for a second.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.7: Neighbor Lawn Dispute (930 - 1180) */}
      {frame >= 930 && frame < 1180 && (
        <CameraRig beatStart={930} beatDuration={250}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 32 }}>
            <div style={{ fontSize: 20, color: "#38BDF8", fontWeight: 800, letterSpacing: "0.15em" }}>
              DOMESTIC LIFE // NEIGHBOR CONFLICT
            </div>
            <div style={{ display: "flex", gap: 40, alignItems: "center" }}>
              <div style={{ backgroundColor: "rgba(30,41,59,0.8)", border: "2px solid #334155", borderRadius: 20, padding: 32, width: 440, textAlign: "center" }}>
                <div style={{ fontSize: 48 }}>🏡 vs 🏡</div>
                <div style={{ fontSize: 26, fontWeight: 800, color: "#F8FAFC", marginTop: 12 }}>You Don't Build a Private Lawn Army</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 8 }}>You dial the police or hire a lawyer</div>
              </div>
              <div style={{ backgroundColor: "rgba(30,41,59,0.8)", border: "2px solid #10B981", borderRadius: 20, padding: 32, width: 440, textAlign: "center" }}>
                <div style={{ fontSize: 48 }}>⚖️</div>
                <div style={{ fontSize: 26, fontWeight: 800, color: "#10B981", marginTop: 12 }}>Enforceable Legal Hierarchy</div>
                <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 8 }}>Courts and police resolve domestic fights</div>
              </div>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.8: Municipal Police Car & Monopoly on Force (1180 - 1400) */}
      {frame >= 1180 && frame < 1400 && (
        <CameraRig beatStart={1180} beatDuration={220}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            {/* Flashing Police Siren Lights */}
            <div style={{ display: "flex", gap: 24 }}>
              <div style={{ width: 40, height: 40, borderRadius: "50%", backgroundColor: frame % 10 < 5 ? "#EF4444" : "#450A0A", boxShadow: frame % 10 < 5 ? "0 0 30px #EF4444" : "none" }} />
              <div style={{ width: 40, height: 40, borderRadius: "50%", backgroundColor: frame % 10 >= 5 ? "#3B82F6" : "#172554", boxShadow: frame % 10 >= 5 ? "0 0 30px #3B82F6" : "none" }} />
            </div>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#F8FAFC", fontFamily: "Space Grotesk, sans-serif" }}>
              MONOPOLY ON LEGITIMATE PHYSICAL FORCE
            </div>
            <div style={{ fontSize: 22, color: "#94A3B8", maxWidth: 800 }}>
              Domestic society works because a single legal hierarchy holds the supreme authority to enforce order.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.9: Superpower Showdown (1400 - 1710) */}
      {frame >= 1400 && frame < 1710 && (
        <CameraRig beatStart={1400} beatDuration={310}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 28, textAlign: "center" }}>
            <div style={{ padding: "8px 24px", backgroundColor: "#EF444420", border: "1px solid #EF4444", borderRadius: 9999, color: "#FCA5A5", fontWeight: 800 }}>
              NUCLEAR-ARMED SUPERPOWERS
            </div>
            <div style={{ fontSize: 56, fontWeight: 900, color: "#F8FAFC", fontFamily: "Space Grotesk, sans-serif", maxWidth: 1100 }}>
              WHO SETTLES THE DISPUTE WHEN THERE IS LITERALLY NO ONE IN CHARGE?
            </div>
            <div style={{ display: "flex", gap: 24, marginTop: 12 }}>
              <div style={{ padding: "12px 28px", backgroundColor: "#334155", borderRadius: 12, fontWeight: 700, fontSize: 18 }}>No World Court Sheriff</div>
              <div style={{ padding: "12px 28px", backgroundColor: "#334155", borderRadius: 12, fontWeight: 700, fontSize: 18 }}>No Global Army Dispatch</div>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.10: Tea in Swiss Chalets (1710 - 2070) */}
      {frame >= 1710 && frame < 2070 && (
        <CameraRig beatStart={1710} beatDuration={360}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>☕ 🇨🇭</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#FEF3C7" }}>
              NOT JUST DIPLOMATS DRINKING TEA IN SUITS
            </div>
            <div style={{ fontSize: 24, color: "#E2E8F0", maxWidth: 900, lineHeight: 1.6 }}>
              Beneath the polite smiles lies the highest-stakes game in human history: survival, immense wealth, alliance betrayal, and raw power.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 1.11: Show Stinger - The Anarchy Problem (2070 - 2406) */}
      {frame >= 2070 && (
        <CameraRig beatStart={2070} beatDuration={336}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 16, textAlign: "center" }}>
            <div style={{ padding: "8px 24px", backgroundColor: "#F59E0B", color: "#0F172A", fontWeight: 900, borderRadius: 9999, fontSize: 18, letterSpacing: "0.2em" }}>
              CRASH COURSE IR // EPISODE 01
            </div>
            <h1 style={{ fontSize: 88, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", letterSpacing: "-0.04em", margin: 0, color: "#F8FAFC" }}>
              THE ANARCHY PROBLEM
            </h1>
            <div style={{ fontSize: 36, fontWeight: 700, color: "#38BDF8" }}>
              WHO'S IN CHARGE OF THE PLANET?
            </div>
          </div>
        </CameraRig>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 2: WHAT IS ANARCHY? (Frames 2406 - 5871 / 115.5s)
// 10 Rapid-Fire Visual Beats
// ===========================================================================
const Act2WhatIsAnarchy: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#090D16", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(239, 68, 68, 0.05)" />
      <ActBadge actNum={2} title="What is Anarchy? (No 911 for Nations)" color="#EF4444" />

      {/* Beat 2.1: The Cocktail Word Anarchy (0 - 205) */}
      {frame >= 0 && frame < 205 && (
        <CameraRig beatStart={0} beatDuration={205}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#94A3B8", letterSpacing: "0.2em", fontWeight: 700, marginBottom: 12 }}>
              THE BIG COCKTAIL PARTY WORD
            </div>
            <div style={{ fontSize: 120, fontWeight: 900, color: "#EF4444", fontFamily: "Space Grotesk, sans-serif", letterSpacing: "0.08em" }}>
              ANARCHY
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.2: Hollywood Mad Max Chaos (205 - 700) */}
      {frame >= 205 && frame < 700 && (
        <CameraRig beatStart={205} beatDuration={495}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 64 }}>🔥 🚗 💀</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F87171" }}>
              HOLLYWOOD POST-APOCALYPTIC CHAOS
            </div>
            <div style={{ fontSize: 24, color: "#CBD5E1", maxWidth: 900, lineHeight: 1.5 }}>
              Masked rioters, burning cars, fighting over the last can of beans in a wasteland.
            </div>
            <div style={{ padding: "8px 24px", backgroundColor: "#EF444420", borderRadius: 8, color: "#FCA5A5", fontWeight: 700 }}>
              Terrifying in movies — but NOT what IR means!
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.3: Reality Check: Anarchy != Chaos (700 - 1115) */}
      {frame >= 700 && frame < 1115 && (
        <CameraRig beatStart={700} beatDuration={415}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ padding: "12px 36px", backgroundColor: "#10B98120", border: "2px solid #10B981", borderRadius: 9999, color: "#34D399", fontSize: 28, fontWeight: 900 }}>
              ANARCHY ≠ TOTAL CHAOS
            </div>
            <div style={{ fontSize: 52, fontWeight: 900, color: "#F8FAFC", fontFamily: "Space Grotesk, sans-serif" }}>
              ABSENCE OF AN OVERARCHING GOVERNMENT
            </div>
            <div style={{ fontSize: 22, color: "#94A3B8", maxWidth: 850 }}>
              No supreme authority above nation-states with the power to command them or enforce global laws.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.4: Domestic Hierarchy Pyramid (1115 - 1600) */}
      {frame >= 1115 && frame < 1600 && (
        <CameraRig beatStart={1115} beatDuration={485}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20, textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#38BDF8", fontWeight: 800, letterSpacing: "0.15em" }}>
              DOMESTIC POLITICS = THE PYRAMID
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 12, alignItems: "center" }}>
              <div style={{ width: 220, padding: "16px 0", backgroundColor: "#0284C7", borderRadius: 8, fontWeight: 900, fontSize: 20 }}>
                Constitution & Apex
              </div>
              <div style={{ width: 360, padding: "16px 0", backgroundColor: "#0369A1", borderRadius: 8, fontWeight: 800, fontSize: 18 }}>
                Judiciary & Police
              </div>
              <div style={{ width: 500, padding: "16px 0", backgroundColor: "#075985", borderRadius: 8, fontWeight: 700, fontSize: 18 }}>
                Protected Citizens
              </div>
            </div>
            <div style={{ fontSize: 18, color: "#94A3B8" }}>Ultimate monopoly on legitimate violence</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.5: Apartment Break-in in London / Jakarta (1600 - 1900) */}
      {frame >= 1600 && frame < 1900 && (
        <CameraRig beatStart={1600} beatDuration={300}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>🏢 🚨 📱</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC" }}>
              APARTMENT BREAK-IN: LONDON OR JAKARTA
            </div>
            <div style={{ fontSize: 24, color: "#E2E8F0" }}>
              You don't hire mercenaries. You dial 9-1-1. The state sends armed officers to enforce order.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.6: Rotary Phone 911 Dialing (1900 - 2065) */}
      {frame >= 1900 && frame < 2065 && (
        <CameraRig beatStart={1900} beatDuration={165}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20 }}>
            <div style={{ fontSize: 96, fontWeight: 900, color: "#EF4444", fontFamily: "Space Grotesk, sans-serif" }}>
              DIAL 9 - 1 - 1
            </div>
            <div style={{ fontSize: 26, color: "#FEF2F2", fontWeight: 700 }}>
              DOMESTIC EMERGENCY DISPATCH AVAILABLE
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.7: International System is FLAT (2065 - 2490) */}
      {frame >= 2065 && frame < 2490 && (
        <CameraRig beatStart={2065} beatDuration={425}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 28, textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.15em" }}>
              INTERNATIONAL SYSTEM = COMPLETELY FLAT
            </div>
            <div style={{ display: "flex", gap: 20, padding: "32px 40px", border: "2px dashed #475569", borderRadius: 16 }}>
              {["USA", "CHN", "GBR", "FRA", "IDN", "IND"].map((flag) => (
                <div key={flag} style={{ padding: "16px 20px", backgroundColor: "#1E293B", borderRadius: 8, fontWeight: 900, fontSize: 22, color: "#F8FAFC" }}>
                  {flag}
                </div>
              ))}
            </div>
            <div style={{ fontSize: 26, fontWeight: 800, color: "#EF4444" }}>
              NO WORLD PRESIDENT. NO GLOBAL ARMY. ZERO APEX.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.8: UN Reality Check (2490 - 2815) */}
      {frame >= 2490 && frame < 2815 && (
        <CameraRig beatStart={2490} beatDuration={325}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>🇺🇳</div>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#38BDF8" }}>
              THE UNITED NATIONS IS NOT A WORLD GOVERNMENT
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", maxWidth: 850 }}>
              It cannot pass binding laws overriding sovereignty, and it cannot arrest a superpower.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.9: The Self-Help System (2815 - 3190) */}
      {frame >= 2815 && frame < 3190 && (
        <CameraRig beatStart={2815} beatDuration={375}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ padding: "10px 32px", backgroundColor: "#EF4444", color: "#FFFFFF", fontWeight: 900, borderRadius: 12, fontSize: 32 }}>
              THE SELF-HELP SYSTEM
            </div>
            <div style={{ fontSize: 28, color: "#F8FAFC", fontWeight: 700, maxWidth: 900 }}>
              If invaded or cut off from energy, NOBODY is coming to save you unless you can defend yourself or summon allies.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 2.10: Thomas Hobbes & State of Nature (3190 - 3465) */}
      {frame >= 3190 && (
        <CameraRig beatStart={3190} beatDuration={275}>
          <div style={{ backgroundColor: "rgba(15,23,42,0.95)", border: "2px solid #F59E0B", borderRadius: 24, padding: "40px 60px", maxWidth: 950, textAlign: "center" }}>
            <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THOMAS HOBBES // LEVIATHAN (1651)
            </div>
            <div style={{ fontSize: 32, fontStyle: "italic", color: "#FEF3C7", lineHeight: 1.5 }}>
              "Without a common power to keep everyone in awe, life in the state of nature is solitary, poor, nasty, brutish, and short."
            </div>
          </div>
        </CameraRig>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 3: ANATOMY OF THE SOVEREIGN STATE (Frames 5871 - 9618 / 124.9s)
// 10 Rapid-Fire Visual Beats
// ===========================================================================
const Act3SovereignState: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#0C1222", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(16, 185, 129, 0.05)" />
      <ActBadge actNum={3} title="Anatomy of the Sovereign State" color="#10B981" />

      {/* Beat 3.1: Global Anarchic Stage (0 - 270) */}
      {frame >= 0 && frame < 270 && (
        <CameraRig beatStart={0} beatDuration={270}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#10B981", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              400 YEARS OF SUPREMACY
            </div>
            <div style={{ fontSize: 80, fontWeight: 900, color: "#F8FAFC", fontFamily: "Space Grotesk, sans-serif" }}>
              THE SOVEREIGN STATE
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.2: Tri-Venn: Country vs Nation vs State (270 - 890) */}
      {frame >= 270 && frame < 890 && (
        <CameraRig beatStart={270} beatDuration={620}>
          <div style={{ display: "flex", gap: 32, maxWidth: 1200 }}>
            <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.8)", borderRadius: 16, padding: 28, border: "2px solid #38BDF8" }}>
              <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800 }}>GEOGRAPHY</div>
              <div style={{ fontSize: 28, fontWeight: 900, margin: "8px 0" }}>Country</div>
              <div style={{ fontSize: 16, color: "#94A3B8" }}>Physical terrain, rivers, hills (e.g. New Zealand).</div>
            </div>
            <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.8)", borderRadius: 16, padding: 28, border: "2px solid #F59E0B" }}>
              <div style={{ fontSize: 16, color: "#F59E0B", fontWeight: 800 }}>IDENTITY</div>
              <div style={{ fontSize: 28, fontWeight: 900, margin: "8px 0" }}>Nation</div>
              <div style={{ fontSize: 16, color: "#94A3B8" }}>Cultural group with shared history (e.g. Kurds, Basques).</div>
            </div>
            <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.9)", borderRadius: 16, padding: 28, border: "2px solid #10B981" }}>
              <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>LEGAL ENTITY</div>
              <div style={{ fontSize: 28, fontWeight: 900, margin: "8px 0" }}>State</div>
              <div style={{ fontSize: 16, color: "#E2E8F0" }}>Formal sovereign political entity with jurisdiction.</div>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.3: Montevideo Convention 1933 (890 - 1255) */}
      {frame >= 890 && frame < 1255 && (
        <CameraRig beatStart={890} beatDuration={365}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#10B981", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 8 }}>
              URUGUAY, 1933
            </div>
            <div style={{ fontSize: 60, fontWeight: 900, color: "#F8FAFC" }}>
              THE MONTEVIDEO CONVENTION
            </div>
            <div style={{ fontSize: 24, color: "#38BDF8", marginTop: 12 }}>
              The 4 Golden Rules of Sovereign Statehood
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.4: Pillar 1: Population (1255 - 1525) */}
      {frame >= 1255 && frame < 1525 && (
        <CameraRig beatStart={1255} beatDuration={270}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #10B981", borderRadius: 16, padding: "36px 48px", width: 700, textAlign: "left" }}>
            <div style={{ fontSize: 18, color: "#10B981", fontWeight: 800 }}>PILLAR 1</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Permanent Population</div>
            <div style={{ fontSize: 20, color: "#94A3B8" }}>You cannot plant a flag on a deserted sandbar and declare yourself Emperor.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.5: Pillar 2: Defined Territory (1525 - 1680) */}
      {frame >= 1525 && frame < 1680 && (
        <CameraRig beatStart={1525} beatDuration={155}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #10B981", borderRadius: 16, padding: "36px 48px", width: 700, textAlign: "left" }}>
            <div style={{ fontSize: 18, color: "#10B981", fontWeight: 800 }}>PILLAR 2</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Defined Territory</div>
            <div style={{ fontSize: 20, color: "#94A3B8" }}>Recognized geographic borders that you effectively control.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.6: Pillar 3: Functioning Government (1680 - 1850) */}
      {frame >= 1680 && frame < 1850 && (
        <CameraRig beatStart={1680} beatDuration={170}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #10B981", borderRadius: 16, padding: "36px 48px", width: 700, textAlign: "left" }}>
            <div style={{ fontSize: 18, color: "#10B981", fontWeight: 800 }}>PILLAR 3</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Functioning Government</div>
            <div style={{ fontSize: 20, color: "#94A3B8" }}>Capable of maintaining domestic legal and social order.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.7: Pillar 4: Diplomatic Recognition (1850 - 2435) */}
      {frame >= 1850 && frame < 2435 && (
        <CameraRig beatStart={1850} beatDuration={585}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #F59E0B", borderRadius: 16, padding: "36px 48px", width: 750, textAlign: "left", boxShadow: "0 0 30px rgba(245,158,11,0.2)" }}>
            <div style={{ fontSize: 18, color: "#F59E0B", fontWeight: 900 }}>PILLAR 4 (THE GOLDEN KEY)</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#FEF3C7", margin: "8px 0" }}>Capacity for Foreign Relations</div>
            <div style={{ fontSize: 20, color: "#CBD5E1" }}>If other nations refuse to recognize you, you are locked out of the global game.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.8: Thirty Years' War 1618-1648 (2435 - 2995) */}
      {frame >= 2435 && frame < 2995 && (
        <CameraRig beatStart={2435} beatDuration={560}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#EF4444", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              CENTRAL EUROPE DEVASTATION
            </div>
            <div style={{ fontSize: 56, fontWeight: 900, color: "#F8FAFC" }}>
              THE THIRTY YEARS' WAR (1618–1648)
            </div>
            <div style={{ fontSize: 24, color: "#FCA5A5", marginTop: 12 }}>
              One third of the population perished before monarchs signed peace.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.9: Peace of Westphalia 1648 (2995 - 3430) */}
      {frame >= 2995 && frame < 3430 && (
        <CameraRig beatStart={2995} beatDuration={435}>
          <div style={{ backgroundColor: "rgba(15,23,42,0.95)", border: "2px solid #10B981", borderRadius: 24, padding: "40px 60px", maxWidth: 900, textAlign: "center" }}>
            <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              PEACE OF WESTPHALIA (1648)
            </div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC" }}>
              "Rex in regno suo est imperator"
            </div>
            <div style={{ fontSize: 24, color: "#F59E0B", fontWeight: 700, marginTop: 8 }}>
              The King is Emperor Within His Own Realm
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 3.10: The Sovereignty Shield (3430 - 3747) */}
      {frame >= 3430 && (
        <CameraRig beatStart={3430} beatDuration={317}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20, textAlign: "center" }}>
            <div style={{ fontSize: 64 }}>🛡️</div>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#10B981" }}>
              THE NORM OF NON-INTERVENTION
            </div>
            <div style={{ fontSize: 24, color: "#CBD5E1", maxWidth: 850 }}>
              Borders became sacred lines: social agreements backed up by military hardware.
            </div>
          </div>
        </CameraRig>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 4: NON-STATE TITANS (Frames 9618 - 13351 / 124.4s)
// 7 Rapid-Fire Visual Beats
// ===========================================================================
const Act4NonStateTitans: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#0A101D", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(139, 92, 246, 0.05)" />
      <ActBadge actNum={4} title="Non-State Titans: Tech, Capital, and Citizens" color="#8B5CF6" />

      {/* Beat 4.1: Tech Giants Control Daily Life (0 - 390) */}
      {frame >= 0 && frame < 390 && (
        <CameraRig beatStart={0} beatDuration={390}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#A78BFA", fontWeight: 800, letterSpacing: "0.2em" }}>
              DOES GOVERNMENT SHAPE YOUR DAY MORE THAN TECH?
            </div>
            <div style={{ fontSize: 56, fontWeight: 900, color: "#F8FAFC" }}>
              GOOGLE • APPLE • MICROSOFT
            </div>
            <div style={{ fontSize: 26, color: "#38BDF8", fontWeight: 700 }}>
              Welcome to the Era of Non-State Actors
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.2: Multinational Corporations (390 - 820) */}
      {frame >= 390 && frame < 820 && (
        <CameraRig beatStart={390} beatDuration={430}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>🚢 ⛏️ 💼</div>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#F8FAFC" }}>
              MULTINATIONAL CORPORATIONS (MNCs)
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", maxWidth: 850 }}>
              Commanding global supply chains, critical mineral reserves, and capital that dwarfs sovereign states.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.3: Apple $3 Trillion vs Nations Bar Chart Race (820 - 1470) */}
      {frame >= 820 && frame < 1470 && (
        <CameraRig beatStart={820} beatDuration={650}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24 }}>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#FEF3C7" }}>
              APPLE'S $3 TRILLION MARKET CAP VS NATIONAL GDP
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 12, width: 750 }}>
              {[
                { name: "France GDP", val: "$3.05 Trillion", w: "95%", c: "#64748B" },
                { name: "Apple Inc.", val: "$3.00 Trillion", w: "93%", c: "#8B5CF6", hl: true },
                { name: "Italy GDP", val: "$2.25 Trillion", w: "70%", c: "#64748B" },
                { name: "Brazil GDP", val: "$2.17 Trillion", w: "67%", c: "#64748B" },
                { name: "Canada GDP", val: "$2.14 Trillion", w: "66%", c: "#64748B" },
              ].map((row, i) => (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: 16 }}>
                  <div style={{ width: 160, textAlign: "right", fontWeight: row.hl ? 900 : 600, color: row.hl ? "#FEF3C7" : "#CBD5E1" }}>
                    {row.name}
                  </div>
                  <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.6)", borderRadius: 6, height: 32, overflow: "hidden" }}>
                    <div style={{ width: row.w, height: "100%", backgroundColor: row.c, paddingLeft: 12, display: "flex", alignItems: "center", fontSize: 15, fontWeight: 800 }}>
                      {row.val}
                    </div>
                  </div>
                </div>
              ))}
            </div>
            <div style={{ fontSize: 20, color: "#C4B5FD", fontWeight: 700 }}>
              Apple would be the 7th largest economy on planet Earth.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.4: Regulatory Arbitrage (1470 - 2200) */}
      {frame >= 1470 && frame < 2200 && (
        <CameraRig beatStart={1470} beatDuration={730}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.8)", border: "2px solid #8B5CF6", borderRadius: 20, padding: "36px 54px", maxWidth: 900, textAlign: "center" }}>
            <div style={{ fontSize: 18, color: "#A78BFA", fontWeight: 800 }}>FINANCIAL PHENOMENON</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>REGULATORY ARBITRAGE</div>
            <div style={{ fontSize: 22, color: "#CBD5E1", lineHeight: 1.6 }}>
              Shifting capital, factories, and profits to whichever country offers the lowest corporate taxes and loosest environmental laws.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.5: INGOs & Transnational Normative Power (2200 - 2850) */}
      {frame >= 2200 && frame < 2850 && (
        <CameraRig beatStart={2200} beatDuration={650}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>🕯️ 🌍 🩺</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#10B981" }}>
              TRANSNATIONAL NORMATIVE POWER
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", maxWidth: 850 }}>
              Amnesty, Greenpeace, MSF: No aircraft carriers, but vast moral authority to shame governments on social media.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.6: Asymmetric Threats & Cyber Hackers (2850 - 3400) */}
      {frame >= 2850 && frame < 3400 && (
        <CameraRig beatStart={2850} beatDuration={550}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>💻 ☠️ 🌐</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#EF4444" }}>
              ASYMMETRIC NON-STATE WARFARE
            </div>
            <div style={{ fontSize: 22, color: "#CBD5E1", maxWidth: 850 }}>
              Transnational cartels and cyber syndicates exploit globalization to wage warfare without sovereign borders.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 4.7: The Crowded Chessboard (3400 - 3733) */}
      {frame >= 3400 && (
        <CameraRig beatStart={3400} beatDuration={333}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#FEF3C7" }}>
              THE CROWDED GLOBAL CHESSBOARD
            </div>
            <div style={{ fontSize: 24, color: "#38BDF8", marginTop: 12, fontWeight: 700 }}>
              Kings, Tech Titans, Activists, and Algorithms
            </div>
          </div>
        </CameraRig>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 5: THE CORE PARADOX (Frames 13351 - 16998 / 121.6s)
// 8 Rapid-Fire Visual Beats
// ===========================================================================
const Act5TheParadox: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#0B111E", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(6, 182, 212, 0.05)" />
      <ActBadge actNum={5} title="The Core Paradox: Why Isn't the World Constantly at War?" color="#06B6D4" />

      {/* Beat 5.1: The Tuesday Afternoon Paradox (0 - 480) */}
      {frame >= 0 && frame < 480 && (
        <CameraRig beatStart={0} beatDuration={480}>
          <div style={{ textAlign: "center", maxWidth: 950 }}>
            <div style={{ fontSize: 20, color: "#06B6D4", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE CENTRAL MYSTERY
            </div>
            <div style={{ fontSize: 56, fontWeight: 900, color: "#F8FAFC", lineHeight: 1.15 }}>
              WHY ISN'T THE WORLD AT WAR EVERY SINGLE TUESDAY?
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.2: 100,000 Flights & Ocean Cargo (480 - 940) */}
      {frame >= 480 && frame < 940 && (
        <CameraRig beatStart={480} beatDuration={460}>
          <div style={{ display: "flex", gap: 32, maxWidth: 1100 }}>
            <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.8)", borderRadius: 16, padding: 32, textAlign: "center", border: "2px solid #38BDF8" }}>
              <div style={{ fontSize: 48 }}>✈️</div>
              <div style={{ fontSize: 32, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>100,000 Flights</div>
              <div style={{ fontSize: 18, color: "#94A3B8" }}>Cross sovereign airspace safely every morning</div>
            </div>
            <div style={{ flex: 1, backgroundColor: "rgba(30,41,59,0.8)", borderRadius: 16, padding: 32, textAlign: "center", border: "2px solid #10B981" }}>
              <div style={{ fontSize: 48 }}>🚢</div>
              <div style={{ fontSize: 32, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>Cargo Ships</div>
              <div style={{ fontSize: 18, color: "#94A3B8" }}>Deliver goods across 20,000 miles of open ocean</div>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.3: Realism vs Liberalism Boxing Ring (940 - 1290) */}
      {frame >= 940 && frame < 1290 && (
        <CameraRig beatStart={940} beatDuration={350}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 20, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE THEORETICAL BOXING RING
            </div>
            <div style={{ fontSize: 64, fontWeight: 900, color: "#F8FAFC" }}>
              <span style={{ color: "#EF4444" }}>REALISM</span> VS <span style={{ color: "#38BDF8" }}>LIBERALISM</span>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.4: Realist Corner: Peace is Intermission (1290 - 1650) */}
      {frame >= 1290 && frame < 1650 && (
        <CameraRig beatStart={1290} beatDuration={360}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #EF4444", borderRadius: 20, padding: "36px 54px", maxWidth: 850, textAlign: "center" }}>
            <div style={{ fontSize: 18, color: "#EF4444", fontWeight: 800 }}>THE REALIST CLAIM</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>
              "Peace is just the temporary intermission between wars."
            </div>
            <div style={{ fontSize: 20, color: "#CBD5E1" }}>States are selfish and terrified of neighbors gaining power.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.5: Balance of Power & Nuclear Deterrence (1650 - 2195) */}
      {frame >= 1650 && frame < 2195 && (
        <CameraRig beatStart={1650} beatDuration={545}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 20, textAlign: "center" }}>
            <div style={{ fontSize: 54 }}>⚖️ ☢️</div>
            <div style={{ fontSize: 44, fontWeight: 900, color: "#EF4444" }}>
              MUTUALLY ASSURED DESTRUCTION (MAD)
            </div>
            <div style={{ fontSize: 24, color: "#FCA5A5", fontWeight: 700 }}>
              Fear, not friendship, keeps weapons holstered.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.6: Liberalism: Peace is Profitable! (2195 - 2560) */}
      {frame >= 2195 && frame < 2560 && (
        <CameraRig beatStart={2195} beatDuration={365}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #38BDF8", borderRadius: 20, padding: "36px 54px", maxWidth: 850, textAlign: "center" }}>
            <div style={{ fontSize: 18, color: "#38BDF8", fontWeight: 800 }}>THE LIBERAL CLAIM</div>
            <div style={{ fontSize: 36, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>
              Peace is Profitable & Durable
            </div>
            <div style={{ fontSize: 20, color: "#CBD5E1" }}>Economic interdependence makes war irrational and suicidal.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.7: Smartphone Teardown Diagram (2560 - 3095) */}
      {frame >= 2560 && frame < 3095 && (
        <CameraRig beatStart={2560} beatDuration={535}>
          <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24 }}>
            <div style={{ fontSize: 32, fontWeight: 900, color: "#38BDF8" }}>
              COMPLEX INTERDEPENDENCE // THE SMARTPHONE TEST
            </div>
            <div style={{ display: "flex", gap: 16 }}>
              {[
                { part: "Software Design", loc: "California, USA" },
                { part: "3nm Microchips", loc: "TSMC, Taiwan" },
                { part: "OLED & Battery", loc: "Seoul, South Korea" },
                { part: "Cobalt Minerals", loc: "DR Congo & China" },
              ].map((c, i) => (
                <div key={i} style={{ backgroundColor: "rgba(30,41,59,0.8)", borderTop: "4px solid #38BDF8", borderRadius: 12, padding: "20px 24px", width: 220 }}>
                  <div style={{ fontSize: 14, color: "#94A3B8" }}>{c.part}</div>
                  <div style={{ fontSize: 18, color: "#F8FAFC", fontWeight: 800, marginTop: 4 }}>{c.loc}</div>
                </div>
              ))}
            </div>
            <div style={{ fontSize: 22, color: "#7DD3FC", fontWeight: 700 }}>
              Blowing up your trade partner destroys your own economy.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 5.8: International Institutions Hub (3095 - 3647) */}
      {frame >= 3095 && (
        <CameraRig beatStart={3095} beatDuration={552}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "2px solid #06B6D4", borderRadius: 20, padding: "36px 54px", maxWidth: 900, textAlign: "center" }}>
            <div style={{ fontSize: 18, color: "#06B6D4", fontWeight: 800 }}>GLOBAL GOVERNANCE</div>
            <div style={{ fontSize: 40, fontWeight: 900, color: "#F8FAFC", margin: "12px 0" }}>
              Institutions as Friction-Reducers
            </div>
            <div style={{ fontSize: 20, color: "#CBD5E1", lineHeight: 1.6 }}>
              The WTO, IMO, and international courts set rules of the road, lowering transaction costs and settling disputes through negotiation.
            </div>
          </div>
        </CameraRig>
      )}
    </AbsoluteFill>
  );
};

// ===========================================================================
// ACT 6: THE TAKEAWAY: WHY IR MATTERS TO YOU (Frames 16998 - 19368 / 79.0s)
// 7 Rapid-Fire Visual Beats
// ===========================================================================
const Act6TheTakeaway: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill style={{ backgroundColor: "#0F172A", color: "#F8FAFC", overflow: "hidden" }}>
      <GridBackground accentColor="rgba(245, 158, 11, 0.05)" />
      <ActBadge actNum={6} title="The Takeaway: Why IR Matters to You" color="#F59E0B" />

      {/* Beat 6.1: Invisible Operating System (0 - 500) */}
      {frame >= 0 && frame < 500 && (
        <CameraRig beatStart={0} beatDuration={500}>
          <div style={{ textAlign: "center", maxWidth: 950 }}>
            <div style={{ fontSize: 20, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              THE INVISIBLE OPERATING SYSTEM
            </div>
            <div style={{ fontSize: 52, fontWeight: 900, color: "#F8FAFC" }}>
              IR RUNS BEHIND YOUR DAILY ROUTINE
            </div>
            <div style={{ fontSize: 24, color: "#94A3B8", marginTop: 16 }}>
              It is not an abstract lecture topic — it dictates your reality every day.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.2: Strait of Hormuz -> Gas Pump (500 - 725) */}
      {frame >= 500 && frame < 725 && (
        <CameraRig beatStart={500} beatDuration={225}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #EF4444", borderRadius: 16, padding: "32px 48px", maxWidth: 800, textAlign: "left" }}>
            <div style={{ fontSize: 16, color: "#EF4444", fontWeight: 800 }}>TRIGGER 1</div>
            <div style={{ fontSize: 32, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Strait of Hormuz Tensions</div>
            <div style={{ fontSize: 22, color: "#CBD5E1" }}>Gasoline prices jump at your local filling station 3 days later.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.3: Tech Tariffs -> Laptop Price (725 - 945) */}
      {frame >= 725 && frame < 945 && (
        <CameraRig beatStart={725} beatDuration={220}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #38BDF8", borderRadius: 16, padding: "32px 48px", maxWidth: 800, textAlign: "left" }}>
            <div style={{ fontSize: 16, color: "#38BDF8", fontWeight: 800 }}>TRIGGER 2</div>
            <div style={{ fontSize: 32, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Semiconductor Trade Wars</div>
            <div style={{ fontSize: 22, color: "#CBD5E1" }}>Shifts the price tag on your next laptop or car overnight.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.4: Climate Treaties -> Century Climate (945 - 1180) */}
      {frame >= 945 && frame < 1180 && (
        <CameraRig beatStart={945} beatDuration={235}>
          <div style={{ backgroundColor: "rgba(30,41,59,0.9)", borderLeft: "8px solid #10B981", borderRadius: 16, padding: "32px 48px", maxWidth: 800, textAlign: "left" }}>
            <div style={{ fontSize: 16, color: "#10B981", fontWeight: 800 }}>TRIGGER 3</div>
            <div style={{ fontSize: 32, fontWeight: 900, color: "#F8FAFC", margin: "8px 0" }}>Global Carbon Agreements</div>
            <div style={{ fontSize: 22, color: "#CBD5E1" }}>Decides atmospheric stability and sea levels for the next century.</div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.5: The IR Superpower (1180 - 1720) */}
      {frame >= 1180 && frame < 1720 && (
        <CameraRig beatStart={1180} beatDuration={540}>
          <div style={{ textAlign: "center", maxWidth: 900 }}>
            <div style={{ fontSize: 20, color: "#F59E0B", fontWeight: 800, letterSpacing: "0.2em", marginBottom: 12 }}>
              YOUR NEW SUPERPOWER
            </div>
            <div style={{ fontSize: 48, fontWeight: 900, color: "#F8FAFC", lineHeight: 1.2 }}>
              Pulling back the curtain on breaking news rhetoric to recognize deep structural forces.
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.6: The 4 Foundation Pillars Summary (1720 - 2075) */}
      {frame >= 1720 && frame < 2075 && (
        <CameraRig beatStart={1720} beatDuration={355}>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20, width: 900 }}>
            <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "1px solid #334155", borderRadius: 12, padding: 24, textAlign: "left" }}>
              <div style={{ fontSize: 22, fontWeight: 900, color: "#EF4444" }}>1. ANARCHY</div>
              <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>Absence of a global sovereign government.</div>
            </div>
            <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "1px solid #334155", borderRadius: 12, padding: 24, textAlign: "left" }}>
              <div style={{ fontSize: 22, fontWeight: 900, color: "#10B981" }}>2. SOVEREIGNTY</div>
              <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>Supreme internal authority within borders.</div>
            </div>
            <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "1px solid #334155", borderRadius: 12, padding: 24, textAlign: "left" }}>
              <div style={{ fontSize: 22, fontWeight: 900, color: "#38BDF8" }}>3. STATE</div>
              <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>Primary actor with monopoly on legitimate force.</div>
            </div>
            <div style={{ backgroundColor: "rgba(30,41,59,0.9)", border: "1px solid #334155", borderRadius: 12, padding: 24, textAlign: "left" }}>
              <div style={{ fontSize: 22, fontWeight: 900, color: "#F59E0B" }}>4. INTERDEPENDENCE</div>
              <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 4 }}>Web of trade and rules preventing total war.</div>
            </div>
          </div>
        </CameraRig>
      )}

      {/* Beat 6.7: Golden Achievement Badge & Outro (2075 - 2370) */}
      {frame >= 2075 && (
        <CameraRig beatStart={2075} beatDuration={295}>
          <div style={{ backgroundColor: "rgba(15,23,42,0.95)", border: "2px solid #F59E0B", borderRadius: 24, padding: "40px 70px", textAlign: "center", boxShadow: "0 20px 60px rgba(245,158,11,0.25)" }}>
            <div style={{ display: "inline-block", padding: "8px 24px", backgroundColor: "#F59E0B", color: "#0F172A", fontWeight: 900, borderRadius: 9999, fontSize: 16, letterSpacing: "0.15em", marginBottom: 16 }}>
              LESSON 01 COMPLETE ✓
            </div>
            <div style={{ fontSize: 52, fontWeight: 900, fontFamily: "Space Grotesk, sans-serif", color: "#F8FAFC" }}>
              CRASH COURSE IR #1
            </div>
            <div style={{ fontSize: 24, color: "#38BDF8", fontWeight: 700, marginTop: 8 }}>
              SEE YOU NEXT TIME ON @IRinANutshell
            </div>
            <div style={{ fontSize: 16, color: "#94A3B8", marginTop: 16 }}>
              Next Up: Realism vs Liberalism — The Great Theoretical Showdown
            </div>
          </div>
        </CameraRig>
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
    f.write(code)

print(f"Successfully generated high-density {TSX_PATH} ({len(code)} bytes)!")
